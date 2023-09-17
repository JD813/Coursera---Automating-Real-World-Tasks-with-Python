#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def generate_report(attachment, title, paragraph):
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  report_paragraph = Paragraph(paragraph, styles["h2"])
  report.build([report_title, report_paragraph])
  return True