def formatFileSize(size: int) -> str:
    if size < 1024:
        return f"{size}B"
    elif size < 1024**2:
        return f"{size / 1024:.2f}kB"
    elif size < 1024**3:
        return f"{size / 1024**2:.2f}MB"
    elif size < 1024**4:
        return f"{size / 1024**3:.2f}GB"
    else:
        return f"{size / 1024**4:.2f}TB"
