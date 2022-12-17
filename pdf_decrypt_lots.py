# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
import PyPDF2
import os
import shutil


def decrypt_pdfs(common_password: str,
                 pdf_folder_path: str = os.getcwd(),
                 output_folder_path: str = None,
                 whether_copy_if_decrypted: bool = True) -> None:
    # 末尾不带/ os.getcwd()
    pdf_path_list: list[str] = os.listdir(pdf_folder_path)

    output_folder_path_path: str = (pdf_folder_path + '\\out\\') \
        if (output_folder_path is None) \
        else (output_folder_path + '\\out\\')

    if not os.path.exists(output_folder_path_path):
        os.makedirs(output_folder_path_path)

    try:
        for each_pdf_path in pdf_path_list:
            # output path
            output_path: str = "".join((output_folder_path_path, os.path.split(each_pdf_path)[-1]))

            if os.path.isfile(each_pdf_path):
                if os.path.splitext(each_pdf_path)[-1].lower() == '.pdf':
                    # Create a PdfFileWriter object
                    writer = PyPDF2.PdfFileWriter()

                    # Open encrypted PDF reader with the PdfFileReader
                    reader = PyPDF2.PdfFileReader(each_pdf_path, strict=False)

                    # Store correct password in a variable password.

                    # Check if the opened reader is actually Encrypted
                    if reader.isEncrypted:

                        # If encrypted, decrypt it with the password
                        reader.decrypt(common_password)

                        # Now, the reader has been unlocked.
                        # Iterate through every page of the reader
                        # and add it to our new reader.
                        for idx in range(reader.numPages):
                            # Get the page at index idx
                            page = reader.getPage(idx)

                            # Add it to the output reader
                            writer.addPage(page)

                        with open(output_path, "wb"):
                            # Open a new reader "decrypted.pdf"
                            writer.write(output_path)

                        # Print success message when Done
                        print("File decrypted Successfully.")
                    else:
                        # If reader is not encrypted, print the
                        # message
                        print("File already decrypted.")
                        if whether_copy_if_decrypted:
                            shutil.copyfile(each_pdf_path, output_path)

    except Exception as e:
        print(e)


password: str = input()

decrypt_pdfs(password)
