#!/usr/bin/env python3
"""Jira MCP server using client certificate + personal token authentication."""

import json
import sys
import os
import urllib.parse

import requests

JIRA_URL = os.environ.get("JIRA_URL", "https://issue.swf.i.mercedes-benz.com")
TOKEN = os.environ.get("JIRA_PERSONAL_TOKEN", "")
CERT = (
    os.path.expanduser(os.environ.get("JIRA_CLIENT_CERT", "~/.ssh/daimler/client.crt")),
    os.path.expanduser(os.environ.get("JIRA_CLIENT_KEY", "~/.ssh/daimler/client.key")),
)
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

TOOLS = [
    {
        "name": "search_issues",
        "description": "Search Jira issues using JQL query",
        "inputSchema": {
            "type": "object",
            "properties": {
                "jql": {"type": "string", "description": "JQL query string"},
                "maxResults": {"type": "integer", "default": 50},
                "fields": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Fields to include in results",
                },
            },
            "required": ["jql"],
        },
    },
    {
        "name": "get_issue",
        "description": "Get a Jira issue by its key",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string", "description": "Issue key, e.g. PROJ-123"}
            },
            "required": ["issue_key"],
        },
    },
    {
        "name": "get_issue_comments",
        "description": "Get all comments for a Jira issue",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string", "description": "Issue key"}
            },
            "required": ["issue_key"],
        },
    },
    {
        "name": "post_issue_comment",
        "description": "Add a comment to a Jira issue",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"},
                "comment": {"type": "string"},
            },
            "required": ["issue_key", "comment"],
        },
    },
    {
        "name": "get_transitions",
        "description": "Get available workflow transitions for a Jira issue",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"}
            },
            "required": ["issue_key"],
        },
    },
    {
        "name": "transition_issue",
        "description": "Transition a Jira issue to a new status",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"},
                "transition_id": {"type": "string", "description": "Transition ID from get_transitions"},
            },
            "required": ["issue_key", "transition_id"],
        },
    },
    {
        "name": "update_issue",
        "description": "Update fields on a Jira issue",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"},
                "fields": {"type": "object", "description": "Fields to update, e.g. {\"summary\": \"new title\"}"},
            },
            "required": ["issue_key", "fields"],
        },
    },
    {
        "name": "list_attachments",
        "description": "List all attachments on a Jira issue with their IDs, filenames, sizes, and MIME types",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string", "description": "Issue key, e.g. PROJ-123"}
            },
            "required": ["issue_key"],
        },
    },
    {
        "name": "download_attachment",
        "description": (
            "Download a Jira attachment by ID and save it locally. "
            "Returns the saved file path and the first 4000 characters of text content "
            "(for .log, .txt, .dlt, .html files). Binary files are saved but not returned as text."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "attachment_id": {"type": "string", "description": "Attachment ID from list_attachments"},
                "filename": {"type": "string", "description": "Original filename (used for save path and MIME detection)"},
                "save_dir": {
                    "type": "string",
                    "description": "Directory to save to. Defaults to /tmp/jira-attachments/",
                },
            },
            "required": ["attachment_id", "filename"],
        },
    },
    {
        "name": "read_saved_attachment",
        "description": "Read a portion of a previously downloaded text attachment (log, html, txt, dlt)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Absolute path to the saved file"},
                "offset_chars": {"type": "integer", "description": "Start character offset (default 0)", "default": 0},
                "length_chars": {"type": "integer", "description": "Number of characters to read (default 8000)", "default": 8000},
            },
            "required": ["file_path"],
        },
    },
    {
        "name": "convert_dlt_to_text",
        "description": (
            "Convert a DLT binary log file to plain text using dlt-viewer. "
            "Returns path to the converted text file and a preview of the content. "
            "Use read_saved_attachment to page through the full converted log."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "dlt_file_path": {"type": "string", "description": "Absolute path to the .dlt file to convert"},
                "filter_apid": {"type": "string", "description": "Optional: filter by Application ID (APID), e.g. 'SFBD'"},
                "filter_ctid": {"type": "string", "description": "Optional: filter by Context ID (CTID)"},
                "filter_text": {"type": "string", "description": "Optional: grep filter text to apply after conversion"},
            },
            "required": ["dlt_file_path"],
        },
    },
    {
        "name": "download_large_attachment",
        "description": (
            "Download a large file attachment from the Jira Large File Transfer plugin. "
            "These files do NOT appear in list_attachments — they are in the 'Large Files' "
            "section of the Jira issue. Filenames are typically mentioned in issue comments. "
            "The issue_id (numeric) is returned by get_issue."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string", "description": "Issue key, e.g. APRICOT-1048114"},
                "issue_id": {"type": "string", "description": "Numeric issue ID, e.g. 16561549 (from get_issue)"},
                "filename": {"type": "string", "description": "Filename as shown in the Large Files section, e.g. 'reproduced issue.dlt'"},
                "mime_type": {
                    "type": "string",
                    "description": "MIME type of the file (default: application/octet-stream)",
                    "default": "application/octet-stream",
                },
                "save_dir": {
                    "type": "string",
                    "description": "Directory to save to. Defaults to /tmp/jira-attachments/",
                },
            },
            "required": ["issue_key", "issue_id", "filename"],
        },
    },
]


def jira_get(path: str, params: dict | None = None) -> dict:
    resp = requests.get(
        f"{JIRA_URL}/rest/api/2{path}",
        headers=HEADERS,
        cert=CERT,
        params=params,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def jira_post(path: str, body: dict) -> dict | None:
    resp = requests.post(
        f"{JIRA_URL}/rest/api/2{path}",
        headers=HEADERS,
        cert=CERT,
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json() if resp.content else None


def jira_put(path: str, body: dict) -> None:
    resp = requests.put(
        f"{JIRA_URL}/rest/api/2{path}",
        headers=HEADERS,
        cert=CERT,
        json=body,
        timeout=30,
    )
    resp.raise_for_status()


def handle_tool_call(name: str, arguments: dict) -> str:
    try:
        if name == "search_issues":
            fields = arguments.get(
                "fields",
                ["summary", "status", "priority", "assignee", "project", "issuetype", "updated"],
            )
            result = jira_get(
                "/search",
                params={
                    "jql": arguments["jql"],
                    "maxResults": arguments.get("maxResults", 50),
                    "fields": ",".join(fields),
                },
            )
            issues = result.get("issues", [])
            total = result.get("total", 0)
            lines = [f"Total: {total} issue(s)\n"]
            for issue in issues:
                key = issue["key"]
                f = issue["fields"]
                lines.append(f"[{key}] {f['summary']}")
                lines.append(f"  Status: {f['status']['name']}")
                if f.get("priority"):
                    lines.append(f"  Priority: {f['priority']['name']}")
                lines.append(f"  Project: {f['project']['name']}")
                if f.get("assignee"):
                    lines.append(f"  Assignee: {f['assignee']['displayName']}")
                lines.append("")
            return "\n".join(lines)

        elif name == "get_issue":
            result = jira_get(f"/issue/{arguments['issue_key']}")
            return json.dumps(result, indent=2)

        elif name == "get_issue_comments":
            result = jira_get(f"/issue/{arguments['issue_key']}/comment")
            comments = result.get("comments", [])
            lines = [f"{len(comments)} comment(s):\n"]
            for c in comments:
                author = c.get("author", {}).get("displayName", "Unknown")
                created = c.get("created", "")[:10]
                body = c.get("body", "")
                lines.append(f"[{created}] {author}:\n{body}\n")
            return "\n".join(lines)

        elif name == "post_issue_comment":
            result = jira_post(
                f"/issue/{arguments['issue_key']}/comment",
                {"body": arguments["comment"]},
            )
            return f"Comment added successfully (id: {result.get('id', '?')})"

        elif name == "get_transitions":
            result = jira_get(f"/issue/{arguments['issue_key']}/transitions")
            transitions = result.get("transitions", [])
            lines = ["Available transitions:"]
            for t in transitions:
                lines.append(f"  id={t['id']} name={t['name']}")
            return "\n".join(lines)

        elif name == "transition_issue":
            jira_post(
                f"/issue/{arguments['issue_key']}/transitions",
                {"transition": {"id": arguments["transition_id"]}},
            )
            return f"Issue {arguments['issue_key']} transitioned successfully."

        elif name == "update_issue":
            jira_put(
                f"/issue/{arguments['issue_key']}",
                {"fields": arguments["fields"]},
            )
            return f"Issue {arguments['issue_key']} updated successfully."

        elif name == "list_attachments":
            import re
            issue_key = arguments["issue_key"]
            # Fetch regular attachments + all comments in one call
            result = jira_get(
                f"/issue/{issue_key}?fields=attachment,comment,summary"
            )
            fields = result.get("fields", {})
            issue_id = result.get("id", "")

            # Regular attachments (small files stored in Jira)
            regular = fields.get("attachment", []) or []
            regular_names = {a["filename"] for a in regular}

            # Large files: discovered from [^filename] markup in comments
            large_files: list[str] = []
            for c in (fields.get("comment", {}) or {}).get("comments", []):
                body = c.get("body", "") or ""
                for fname in re.findall(r"\[\^([^\]]+)\]", body):
                    if fname not in regular_names and fname not in large_files:
                        large_files.append(fname)

            lines = []
            if regular:
                lines.append(f"Regular attachments ({len(regular)}):")
                for a in regular:
                    size_kb = a["size"] // 1024
                    lines.append(
                        f"  [regular] id={a['id']}  {a['filename']}  ({size_kb} KB, {a['mimeType']})"
                    )
            if large_files:
                lines.append(f"\nLarge file attachments found in comments ({len(large_files)}) — download with download_large_attachment (issue_id={issue_id}):")
                for fname in large_files:
                    lines.append(f"  [large]   {fname}")
            lines.append(
                "\n  NOTE: Only large files referenced via [^filename] in comments are auto-discovered. "
                "Files uploaded directly to the Large Files section without a comment reference "
                "cannot be listed via API. Check the issue in your browser for any additional "
                "large files and provide their exact filenames to download them with download_large_attachment."
            )
            if not regular and not large_files:
                return "No attachments found.\n\n  NOTE: Only large files referenced via [^filename] in comments are auto-discovered. " \
                    "Files uploaded directly to the Large Files section without a comment reference " \
                    "cannot be listed via API. Check the issue in your browser for any additional " \
                    "large files and provide their exact filenames to download them with download_large_attachment."
            return "\n".join(lines)

        elif name == "download_attachment":
            import pathlib
            attachment_id = arguments["attachment_id"]
            filename = arguments["filename"]
            save_dir = pathlib.Path(arguments.get("save_dir", "/tmp/jira-attachments")).expanduser()
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir / filename

            resp = requests.get(
                f"{JIRA_URL}/secure/attachment/{attachment_id}/{filename}",
                headers=HEADERS,
                cert=CERT,
                timeout=120,
                stream=True,
            )
            resp.raise_for_status()
            with open(save_path, "wb") as fh:
                for chunk in resp.iter_content(chunk_size=65536):
                    fh.write(chunk)

            size_kb = save_path.stat().st_size // 1024
            result_lines = [f"Saved: {save_path} ({size_kb} KB)"]

            # Return text preview for readable files
            text_exts = {".log", ".txt", ".html", ".htm", ".dlt", ".csv", ".json", ".xml"}
            if save_path.suffix.lower() in text_exts:
                try:
                    with open(save_path, "r", errors="replace") as fh:
                        preview = fh.read(4000)
                    result_lines.append(f"\n--- Content preview (first 4000 chars) ---\n{preview}")
                    if size_kb > 4:
                        result_lines.append(
                            f"\n[File has more content. Use read_saved_attachment tool with file_path={save_path} to read further.]"
                        )
                except Exception as e:
                    result_lines.append(f"(Could not read text content: {e})")
            else:
                result_lines.append("(Binary file — use a dedicated tool to analyse this format.)")

            return "\n".join(result_lines)

        elif name == "read_saved_attachment":
            import pathlib
            file_path = pathlib.Path(arguments["file_path"])
            if not file_path.exists():
                return f"File not found: {file_path}"
            offset = arguments.get("offset_chars", 0)
            length = arguments.get("length_chars", 8000)
            with open(file_path, "r", errors="replace") as fh:
                fh.seek(offset)
                content = fh.read(length)
            file_size = file_path.stat().st_size
            return (
                f"[{file_path.name} — offset {offset}, {len(content)} chars read, file size {file_size} bytes]\n\n"
                + content
            )

        elif name == "convert_dlt_to_text":
            import pathlib
            import subprocess
            dlt_path = pathlib.Path(arguments["dlt_file_path"])
            if not dlt_path.exists():
                return f"DLT file not found: {dlt_path}"
            out_path = dlt_path.with_suffix(".txt")
            # Convert DLT binary → plain text using dlt-viewer CLI
            result = subprocess.run(
                ["dlt-viewer", "-s", "-t", "-c", str(out_path), str(dlt_path)],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if not out_path.exists():
                return (
                    f"dlt-viewer conversion failed.\n"
                    f"stdout: {result.stdout[:500]}\n"
                    f"stderr: {result.stderr[:500]}"
                )
            # Apply optional filters
            filter_text = arguments.get("filter_text")
            filter_apid = arguments.get("filter_apid")
            filter_ctid = arguments.get("filter_ctid")
            if filter_apid or filter_ctid or filter_text:
                filtered_path = out_path.with_suffix(".filtered.txt")
                grep_cmd = ["grep"]
                if filter_apid:
                    grep_cmd += ["-e", filter_apid]
                if filter_ctid:
                    grep_cmd += ["-e", filter_ctid]
                if filter_text:
                    grep_cmd += ["-e", filter_text]
                with open(out_path) as src, open(filtered_path, "w") as dst:
                    subprocess.run(grep_cmd, stdin=src, stdout=dst, timeout=60)
                read_path = filtered_path
            else:
                read_path = out_path
            size_kb = read_path.stat().st_size // 1024
            with open(read_path, "r", errors="replace") as fh:
                preview = fh.read(6000)
            lines = [
                f"Converted: {read_path} ({size_kb} KB)",
                f"Use read_saved_attachment with file_path={read_path} to page through the full log.\n",
                "--- Preview (first 6000 chars) ---",
                preview,
            ]
            if size_kb > 6:
                lines.append(
                    f"\n[{size_kb - 6} KB remaining — use read_saved_attachment with offset_chars=6000]"
                )
            return "\n".join(lines)

        elif name == "download_large_attachment":
            import pathlib, urllib.parse
            issue_key = arguments["issue_key"]
            issue_id = arguments["issue_id"]
            filename = arguments["filename"]
            mime_type = arguments.get("mime_type", "application/octet-stream")
            save_dir = pathlib.Path(arguments.get("save_dir", "/tmp/jira-attachments")).expanduser()
            save_dir.mkdir(parents=True, exist_ok=True)
            safe_name = filename.replace(" ", "_")
            save_path = save_dir / safe_name
            project_key = issue_key.split("-")[0]
            url = (
                f"{JIRA_URL}/plugins/servlet/large-attach/downloadla"
                f"?keyProject={project_key}"
                f"&idIssue={issue_id}"
                f"&name={urllib.parse.quote(filename)}"
                f"&mimeType={urllib.parse.quote(mime_type)}"
            )
            resp = requests.get(
                url, headers=HEADERS, cert=CERT, timeout=300, stream=True,
            )
            resp.raise_for_status()
            with open(save_path, "wb") as fh:
                for chunk in resp.iter_content(chunk_size=65536):
                    fh.write(chunk)
            size_kb = save_path.stat().st_size // 1024
            result_lines = [f"Saved: {save_path} ({size_kb} KB)"]
            text_exts = {".log", ".txt", ".html", ".htm", ".csv", ".json", ".xml"}
            if save_path.suffix.lower() in text_exts:
                with open(save_path, "r", errors="replace") as fh:
                    preview = fh.read(4000)
                result_lines.append(f"\n--- Content preview ---\n{preview}")
            else:
                result_lines.append(
                    f"Binary file saved. If this is a .dlt file, use convert_dlt_to_text "
                    f"with dlt_file_path={save_path}"
                )
            return "\n".join(result_lines)

        else:
            return f"Unknown tool: {name}"

    except requests.HTTPError as e:
        return f"HTTP error {e.response.status_code}: {e.response.text[:300]}"
    except Exception as e:
        return f"Error: {e}"


def send(msg_id, result=None, error=None) -> None:
    resp = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        resp["error"] = error
    else:
        resp["result"] = result
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        msg_id = msg.get("id")
        method = msg.get("method", "")
        params = msg.get("params", {})

        # Notifications have no id — do not respond
        if msg_id is None:
            continue

        if method == "initialize":
            send(
                msg_id,
                {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "jira-onprem", "version": "1.0.0"},
                },
            )
        elif method == "tools/list":
            send(msg_id, {"tools": TOOLS})
        elif method == "tools/call":
            text = handle_tool_call(params.get("name", ""), params.get("arguments", {}))
            send(msg_id, {"content": [{"type": "text", "text": text}]})
        else:
            send(msg_id, error={"code": -32601, "message": f"Method not found: {method}"})


if __name__ == "__main__":
    main()
