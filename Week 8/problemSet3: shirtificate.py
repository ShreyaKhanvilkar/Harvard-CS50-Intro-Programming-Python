from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "B", 40)
        self.cell(200, 80, "CS50 Shirtificate", align="C")


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page(orientation="P", format="A4")
    pdf.set_font("helvetica", "", 25)
    pdf.set_text_color(255,255,255)
    pdf.cell(-210, 240, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
