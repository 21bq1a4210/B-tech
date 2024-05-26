def main():
    # Prompt the user for a file name
    file_name = input("File name: ").strip().lower()

    # Define a dictionary to map file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Extract the file extension
    file_extension = ""
    if "." in file_name:
        file_extension = file_name[file_name.rfind('.'):]

    # Determine the media type
    media_type = media_types.get(file_extension, "application/octet-stream")

    # Output the media type
    print(media_type)

if __name__ == "__main__":
    main()
