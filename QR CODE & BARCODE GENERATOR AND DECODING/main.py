import qrcode
import barcode
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
import cv2
import os


# QR code
def create_qr_code(data, filename):
    # Ensure the directory exists
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    
    # Save the QR code image
    img.save(f"qr_codes/{filename}.png")
    print(f"QR Code saved as qr_codes/{filename}.png")


# Bar code
def create_barcode(data, filename):
    # Use Code128 format for barcodes
    barcode_class = barcode.get_barcode_class('code128')
    barcode_instance = barcode_class(data, writer=ImageWriter())

    # Ensure the directory exists
    if not os.path.exists('barcodes'):
        os.makedirs('barcodes')

    # Save Barcode
    barcode_instance.save(f"barcodes/{filename}")
    print(f"Barcode saved as barcodes/{filename}.png")



# QR de-code
def decode_qr_code(filepath):
    # Decode QR Code
    img = cv2.imread(filepath)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(f"QR Code Data: {obj.data.decode('utf-8')}")


# Bar de-code
def decode_barcode(filepath):
    # Decode Barcode
    img = cv2.imread(filepath)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(f"Barcode Data: {obj.data.decode('utf-8')}")




# main
def main():
    while True:
        # Ask user for choice
        print("\nChoose an option:")
        print("1. Create QR Code and Barcode")
        print("2. Decode QR Code")
        print("3. Decode Barcode")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Take Student ID and Name
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")

            # Combine ID and Name
            data = f"{student_id}-{student_name}"
            filename = student_id  # Use student ID as filename

            # Create QR and Barcode
            create_qr_code(data, filename)
            create_barcode(student_id, filename)

        elif choice == '2':
            # Decode QR Code
            filename = input("Enter the filename of the QR code (without extension): ")
            filepath = f"qr_codes/{filename}.png"
            if os.path.exists(filepath):
                print("\nDecoding QR Code:")
                decode_qr_code(filepath)
            else:
                print("QR code file not found.")

        elif choice == '3':
            # Decode Barcode
            filename = input("Enter the filename of the barcode (without extension): ")
            filepath = f"barcodes/{filename}.png"
            if os.path.exists(filepath):
                print("\nDecoding Barcode:")
                decode_barcode(filepath)
            else:
                print("Barcode file not found.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice..")


if __name__ == "__main__":
    main()
