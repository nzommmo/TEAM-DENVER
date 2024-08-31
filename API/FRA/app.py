from flask import Flask, request, jsonify, send_file
import random
from flask_cors import CORS
import string
import json
from datetime import datetime, timedelta
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
import PyPDF2

app = Flask(__name__)
CORS(app)  # Enable CORS
app.secret_key = 'your_secret_key_here'

banks = {
    # ... (your banks configuration)
}

def generate_unique_code(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_transactions(num_transactions):
    transactions = []
    date = datetime.now() - timedelta(days=30)
    balance = 5000.00

    for _ in range(num_transactions):
        amount = round(random.uniform(-500, 500), 2)
        balance += amount
        transactions.append({
            "date": date.strftime("%Y-%m-%d"),
            "description": random.choice(["Grocery Store", "Online Shopping", "Salary Deposit", "Utility Bill", "Restaurant"]),
            "amount": amount,
            "balance": round(balance, 2)
        })
        date += timedelta(days=random.randint(1, 3))

    return transactions

def generate_fake_statement(bank, original_transactions):
    fake_transactions = original_transactions.copy()
    bank_info = banks[bank].copy()
    
    num_tweaks = random.randint(1, 3)
    tweaks = []
    
    for _ in range(num_tweaks):
        tweak = random.choice(["font", "color", "alignment", "date"])
        
        if tweak == "font" and "font" not in tweaks:
            new_font = random.choice(["Helvetica", "Times-Roman", "Courier"])
            bank_info["font"] = new_font
            bank_info["header_style"].fontName = new_font + "-Bold"
            bank_info["body_style"].fontName = new_font
            tweaks.append(f"Changed font to {new_font}")
        elif tweak == "color" and "color" not in tweaks:
            new_color = random.choice([colors.blue, colors.red, colors.green, colors.purple])
            bank_info["color"] = new_color
            bank_info["header_style"].textColor = new_color
            tweaks.append(f"Changed color to {new_color}")
        elif tweak == "alignment" and "alignment" not in tweaks:
            new_alignment = random.choice(["LEFT", "CENTER", "RIGHT"])
            bank_info["alignment"] = new_alignment
            tweaks.append(f"Changed alignment to {new_alignment}")
        elif tweak == "date" and "date" not in tweaks:
            date_shift = random.randint(1, 5)
            for transaction in fake_transactions:
                date = datetime.strptime(transaction['date'], "%Y-%m-%d")
                new_date = date + timedelta(days=date_shift)
                transaction['date'] = new_date.strftime("%Y-%m-%d")
            tweaks.append(f"Shifted all dates by {date_shift} days")
    
    return fake_transactions, bank_info, tweaks

def save_statement_info(statement_number, bank, is_fake, tweaks=None):
    info = {
        "statement_number": statement_number,
        "bank": bank,
        "is_fake": is_fake,
        "tweaks": tweaks if is_fake else None
    }
    
    try:
        with open('statements_info.json', 'r') as file:
            statements_info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        statements_info = []

    statements_info.append(info)

    with open('statements_info.json', 'w') as file:
        json.dump(statements_info, file, indent=4)

@app.route('/generate', methods=['POST'])
def generate_statement():
    data = request.json
    bank = data.get('bank')
    if not bank or bank not in banks:
        return jsonify({"error": "Invalid bank name"}), 400

    transactions = generate_transactions(20)
    bank_info = banks[bank]
    statement_number = generate_unique_code()
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=50, bottomMargin=50, leftMargin=40, rightMargin=40)
    elements = []

    elements.append(Spacer(1, 12))
    elements.append(Paragraph(bank, bank_info['header_style']))
    elements.append(Paragraph(bank_info['address'], bank_info['body_style']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Statement Date: {datetime.now().strftime('%Y-%m-%d')}", bank_info['body_style']))
    elements.append(Paragraph(f"Statement Number: {statement_number}", bank_info['body_style']))
    elements.append(Spacer(1, 12))

    data = [['Date', 'Description', 'Amount', 'Balance']]
    for transaction in transactions:
        data.append([
            transaction['date'],
            transaction['description'],
            f"${transaction['amount']:.2f}",
            f"${transaction['balance']:.2f}"
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), bank_info['color']),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), bank_info['header_style'].fontName),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), bank_info['body_style'].fontName),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, bank_info['color'])
    ]))

    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    
    save_statement_info(statement_number, bank, is_fake=False)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        download_name=f'{bank.replace(" ", "_")}_statement_{statement_number}.pdf',
        as_attachment=True
    )

@app.route('/generate_fake', methods=['POST'])
def generate_fake_statement():
    data = request.json
    bank = data.get('bank')
    if not bank or bank not in banks:
        return jsonify({"error": "Invalid bank name"}), 400

    original_transactions = generate_transactions(20)
    fake_transactions, fake_bank_info, tweaks = generate_fake_statement(bank, original_transactions)
    statement_number = generate_unique_code()
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=50, bottomMargin=50, leftMargin=40, rightMargin=40)
    elements = []

    elements.append(Spacer(1, 12))
    elements.append(Paragraph(bank, fake_bank_info['header_style']))
    elements.append(Paragraph(fake_bank_info['address'], fake_bank_info['body_style']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Statement Date: {datetime.now().strftime('%Y-%m-%d')}", fake_bank_info['body_style']))
    elements.append(Paragraph(f"Statement Number: {statement_number}", fake_bank_info['body_style']))
    elements.append(Spacer(1, 12))

    data = [['Date', 'Description', 'Amount', 'Balance']]
    for transaction in fake_transactions:
        data.append([
            transaction['date'],
            transaction['description'],
            f"${transaction['amount']:.2f}",
            f"${transaction['balance']:.2f}"
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), fake_bank_info['color']),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), fake_bank_info['header_style'].fontName),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), fake_bank_info['body_style'].fontName),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, fake_bank_info['color'])
    ]))

    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    
    save_statement_info(statement_number, bank, is_fake=True, tweaks=tweaks)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        download_name=f'{bank.replace(" ", "_")}_fake_statement_{statement_number}.pdf',
        as_attachment=True
    )

@app.route('/verify', methods=['POST'])
def verify_statement():
    data = request.json
    statement_number = data.get('statement_number')
    
    if not statement_number:
        return jsonify({"error": "Statement number is required"}), 400

    try:
        with open('statements_info.json', 'r') as file:
            statements_info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"error": "No statement information found"}), 404

    for info in statements_info:
        if info['statement_number'] == statement_number:
            return jsonify(info)

    return jsonify({"error": "Statement not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
