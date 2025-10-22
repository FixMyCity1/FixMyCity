# TODO: Fix submit_report.py MIME Type Issue

- [x] Add import for mimetypes module at the top of user/submit_report.py
- [x] Modify handle_file_upload function to detect MIME type from file name and store it in uploaded_file_data
- [x] Modify send_request function to use the dynamic MIME type in the files dict
