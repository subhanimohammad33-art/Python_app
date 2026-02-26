from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_bullet(self, text):
        self.set_font('Arial', '', 10)
        self.cell(5)
        self.cell(2, 5, chr(149), 0, 0)
        self.multi_cell(0, 5, text)
        self.ln(1)

def create_resume():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- CONTACT INFO ---
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'SUBHANI MOHAMMAD', 0, 1, 'C')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, 'Hyderabad, Telangana | +91 7660845665 | subhanimohammad33@gmail.com', 0, 1, 'C')
    pdf.ln(5)

    # --- SUMMARY ---
    pdf.chapter_title('PROFESSIONAL SUMMARY')
    pdf.chapter_body(
        "Results-oriented Senior Python Developer with 6+ years of experience architecting and deploying "
        "scalable backend systems and Microservices. Expert in Python, FastAPI, and Kubernetes. Proven track "
        "record of leading development teams, reducing system latency by 40%, and implementing containerized "
        "deployment workflows. Passionate about clean code standards and mentoring."
    )

    # --- SKILLS ---
    pdf.chapter_title('TECHNICAL SKILLS')
    pdf.add_bullet("Languages: Python, SQL, Shell Scripting.")
    pdf.add_bullet("Frameworks & Tech: FastAPI, Flask, Pytest, Microservices.")
    pdf.add_bullet("Databases: PostgreSQL, OpenSearch, ElasticSearch.")
    pdf.add_bullet("Cloud & DevOps: Kubernetes (K8s), Docker, AWS, Azure, Jenkins, Pex, Git.")
    pdf.add_bullet("Architecture: RESTful APIs, System Design, IDAM, CyberArk.")
    pdf.ln(2)

    # --- EXPERIENCE ---
    pdf.chapter_title('PROFESSIONAL EXPERIENCE')

    # TCS
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'TATA CONSULTANCY SERVICES (TCS) | Hyderabad, India', 0, 1)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 5, 'Senior Python Developer | Nov 2022 - Present', 0, 1)
    pdf.ln(1)
    
    pdf.add_bullet("Spearheaded the migration of a monolithic architecture to Microservices using FastAPI and Kubernetes, handling a 40% increase in traffic.")
    pdf.add_bullet("Architected high-performance RESTful APIs and optimized PostgreSQL queries to reduce average response time by 70%.")
    pdf.add_bullet("Mentored a team of 4 junior developers, conducting code reviews and enforcing PEP8 standards.")
    
    # Onsite
    pdf.ln(2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(10)
    pdf.cell(0, 5, 'Onsite Technical Lead - GS CALTEX (Yeosu, South Korea) | 6 Months', 0, 1)
    pdf.ln(1)
    pdf.add_bullet("Selected by leadership to travel onsite to bridge the technical gap between business stakeholders and the offshore development team.")
    pdf.add_bullet("Collaborated directly with client solution architects to finalize AWS cloud infrastructure and Kubernetes cluster requirements.")
    pdf.add_bullet("Managed the User Acceptance Testing (UAT) phase and resolved critical bugs in Python/Django logic to ensure on-time Go-Live.")
    pdf.add_bullet("Facilitated knowledge transfer workshops for the client's internal IT team.")
    pdf.ln(3)

    # Infosys - UPDATED SECTION
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'INFOSYS LIMITED | Hyderabad, India', 0, 1)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 5, 'Senior System Engineer (HPE Project) | Jan 2020 - Nov 2022', 0, 1)
    pdf.ln(1)

    pdf.add_bullet("Engineered end-to-end Python automation scripts for Identity and Access Management (IDAM) lifecycle management, reducing manual provisioning by 40%.")
    pdf.add_bullet("Developed a robust RESTful API layer using Flask to expose complex automation workflows.")
    pdf.add_bullet("Architected and configured the full suite of CyberArk components and managed L3/L4 security operations using ServiceNow.")
    pdf.add_bullet("Designed and optimized the underlying PostgreSQL database schema for high-availability security logging.")
    pdf.ln(2)

    # --- CERTIFICATIONS & EDUCATION ---
    pdf.chapter_title('CERTIFICATIONS & EDUCATION')
    pdf.add_bullet("Infosys Certified Python Associate")
    pdf.add_bullet("Purdue University: Applied Cybersecurity Essentials")
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'B.Tech in Computer Science | SIR C.R REDDY COLLEGE OF ENGINEERING', 0, 1)

    # Output Fix
    pdf.output('Subhani_Mohammad_Resume.pdf')
    print("PDF generated successfully: Subhani_Mohammad_Resume.pdf")

if __name__ == '__main__':
    create_resume()