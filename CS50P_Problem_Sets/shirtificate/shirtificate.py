from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 40)
        self.cell(30, 50, "CS50 Shirtificate", align = "C", center = True)
        self.image("./shirtificate.png", 10, 80, 190)

def main():

    user_name = input("Name: ")
    shirtificate(user_name)

def shirtificate(s):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 25)
    pdf.cell(10, 100, new_y = "NEXT")
    pdf.set_text_color(255, 255, 255)
    pdf.cell(170, 40, f"{s} took CS50", align = 'c', center = True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()