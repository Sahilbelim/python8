from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 10)
pdf.cell(40, 5, 'Powered by FPDF.', 0, 1,)
pdf.cell(40, 5, 'test.', 0, 1,)
pdf.cell(40, 5, 'exam.', 0, 1,)
pdf.output('a.pdf', 'F')