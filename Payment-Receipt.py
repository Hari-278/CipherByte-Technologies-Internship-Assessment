# CREATING PAYMENT RECEIPT
# Creating payment receipts is a pretty common task, be it an e-commerce website or any local store for that matter.
# Here, you have to create our own transaction receipts just by using python. We would be using reportlab to generate the PDFs. Generally, it comes as a built-in package but sometimes it might not be present too. If it's not present, then simply type the following in your terminal

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_payment_receipt(customer_name, amount_paid, payment_method, receipt_number):
    # Create a PDF document
    c = canvas.Canvas(f"payment_receipt_{receipt_number}.pdf", pagesize=letter)

    # Set up fonts
    c.setFont("Helvetica-Bold", 16)

    # Write title
    c.drawCentredString(300, 750, "Payment Receipt")

    # Set up fonts for details
    c.setFont("Helvetica", 12)

    # Write receipt number
    c.drawString(50, 700, f"Receipt Number: {receipt_number}")

    # Write date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(50, 680, f"Date: {date}")

    # Write customer name
    c.drawString(50, 660, f"Customer Name: {customer_name}")

    # Write amount paid
    c.drawString(50, 640, f"Amount Paid: ${amount_paid}")

    # Write payment method
    c.drawString(50, 620, f"Payment Method: {payment_method}")

    # Save the PDF
    c.save()

# Example usage
customer_name = "John Doe"
amount_paid = 100.00
payment_method = "Credit Card"
receipt_number = "20220411"

generate_payment_receipt(customer_name, amount_paid, payment_method, receipt_number)
