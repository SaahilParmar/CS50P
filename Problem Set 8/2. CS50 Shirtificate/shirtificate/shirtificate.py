from fpdf import FPDF

# Initialising FPDF.
shirtificate = FPDF()

# Adding page to pdf file.
shirtificate.add_page()

# Setting font type, style & size.
shirtificate.set_font('helvetica', style='', size=48)

# Setting input in the image.
shirtificate.cell(0, 57, 'CS50 Shirtificate',  align='c')

# Setting image dimensions.
shirtificate.image('shirtificate.png', x=10, y=70, w=190, h=190)

# Setting text color.
shirtificate.set_text_color(255, 255, 255)

# Setting font type, style & size.
shirtificate.set_font('helvetica', style='', size=24)

# Getting user input & setting it in the image.
shirtificate.cell(-190, 253, input('Name: ').strip().title() + ' took CS50',  align='C')

# Getting output.
shirtificate.output('shirtificate.pdf')
