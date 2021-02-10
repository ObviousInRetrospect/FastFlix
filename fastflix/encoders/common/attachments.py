# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List

from fastflix.models.encode import AttachmentTrack
from fastflix.shared import unixy


def image_type(file: Path):
    mime_type = "image/jpeg"
    ext_type = "jpg"
    if file.name.lower().endswith("png"):
        mime_type = "image/png"
        ext_type = "png"
    return mime_type, ext_type


def build_attachments(attachments: List[AttachmentTrack]) -> str:

    commands = []
    for attachment in attachments:
        if attachment.attachment_type == "cover":
            mime_type, ext_type = image_type(attachment.file_path)
            unixy_path = unixy(attachment.file_path)
            commands.append(
                f' -attach "{unixy_path}" -metadata:s:{attachment.outdex} mimetype="{mime_type}" '
                f'-metadata:s:{attachment.outdex}  filename="{attachment.filename}.{ext_type}" '
            )
    return " ".join(commands)
