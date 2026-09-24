import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # Set 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    COLOR_PRIMARY_RED = RGBColor(198, 40, 40)       # #C62828
    COLOR_DARK_RED = RGBColor(183, 28, 28)         # #B71C1C
    COLOR_LIGHT_BG = RGBColor(250, 250, 250)        # #FAFAFA
    COLOR_LIGHT_RED_BG = RGBColor(255, 235, 238)    # #FFEBEE
    COLOR_CARD_BG = RGBColor(255, 255, 255)         # #FFFFFF
    COLOR_TEXT_MAIN = RGBColor(33, 33, 33)          # #212121
    COLOR_TEXT_MUTED = RGBColor(117, 117, 117)      # #757575
    COLOR_WHITE = RGBColor(255, 255, 255)

    def set_slide_background(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, title_text):
        # Header Drop Icon (Teardrop shape)
        icon_shape = slide.shapes.add_shape(MSO_SHAPE.TEAR, Inches(0.6), Inches(0.4), Inches(0.45), Inches(0.55))
        icon_shape.fill.solid()
        icon_shape.fill.fore_color.rgb = COLOR_PRIMARY_RED
        icon_shape.line.fill.background()
        icon_shape.rotation = 180

        # Header Title
        title_box = slide.shapes.add_textbox(Inches(1.15), Inches(0.35), Inches(8.0), Inches(0.7))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = 'Arial'
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_RED

        # Heartbeat pulse line under header
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.15), Inches(1.05), Inches(10.5), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_PRIMARY_RED
        line.line.fill.background()

    def add_slide_badge(slide, slide_num):
        # Bottom left circle badge
        badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.4), Inches(6.6), Inches(0.5), Inches(0.5))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_RED
        badge.line.fill.background()
        tf = badge.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = str(slide_num)
        p.font.name = 'Arial'
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

        # Footer watermark text
        footer_box = slide.shapes.add_textbox(Inches(8.5), Inches(6.8), Inches(4.3), Inches(0.4))
        tf = footer_box.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        p.text = "ShareLife – A Blood Donor Management System"
        p.font.name = 'Arial'
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MUTED

    # ==================== SLIDE 1: Title ====================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, COLOR_CARD_BG)

    # Top Left Decorative Arc
    top_wave = slide1.shapes.add_shape(MSO_SHAPE.TEAR, Inches(-1.5), Inches(-1.5), Inches(4.5), Inches(4.5))
    top_wave.fill.solid()
    top_wave.fill.fore_color.rgb = COLOR_PRIMARY_RED
    top_wave.line.fill.background()

    # Title Text Frame
    title_box1 = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(6.5), Inches(3.0))
    tf1 = title_box1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "ShareLife"
    p.font.name = 'Arial'
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_RED

    p2 = tf1.add_paragraph()
    p2.text = "A Blood Donor Management System"
    p2.font.name = 'Arial'
    p2.font.size = Pt(24)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_TEXT_MAIN
    p2.space_before = Pt(10)

    # Divider pulse line
    line1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(2.7), Inches(4.0), Inches(0.03))
    line1.fill.solid()
    line1.fill.fore_color.rgb = COLOR_PRIMARY_RED
    line1.line.fill.background()

    # Presented By Box
    pres_box = slide1.shapes.add_textbox(Inches(1.2), Inches(3.6), Inches(4.5), Inches(1.5))
    tf_p = pres_box.text_frame
    p_lbl = tf_p.paragraphs[0]
    p_lbl.text = "Presented By"
    p_lbl.font.name = 'Arial'
    p_lbl.font.size = Pt(14)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = COLOR_PRIMARY_RED

    p_val = tf_p.add_paragraph()
    p_val.text = "Satyam Sharma"
    p_val.font.name = 'Arial'
    p_val.font.size = Pt(22)
    p_val.font.bold = True
    p_val.font.color.rgb = COLOR_TEXT_MAIN
    p_val.space_before = Pt(4)

    # Right side graphic - Large Blood Drop Circle Container
    drop_bg = slide1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.0), Inches(1.2), Inches(4.5), Inches(4.5))
    drop_bg.fill.solid()
    drop_bg.fill.fore_color.rgb = COLOR_LIGHT_RED_BG
    drop_bg.line.fill.background()

    big_drop = slide1.shapes.add_shape(MSO_SHAPE.TEAR, Inches(9.0), Inches(1.6), Inches(2.5), Inches(3.4))
    big_drop.fill.solid()
    big_drop.fill.fore_color.rgb = COLOR_PRIMARY_RED
    big_drop.line.fill.background()
    big_drop.rotation = 180

    # Plus sign inside drop
    plus1 = slide1.shapes.add_shape(MSO_SHAPE.CROSS, Inches(9.8), Inches(2.8), Inches(0.9), Inches(0.9))
    plus1.fill.solid()
    plus1.fill.fore_color.rgb = COLOR_WHITE
    plus1.line.fill.background()

    # Bottom wave accent
    bot_wave = slide1.shapes.add_shape(MSO_SHAPE.TEAR, Inches(-1.0), Inches(5.8), Inches(6.0), Inches(3.0))
    bot_wave.fill.solid()
    bot_wave.fill.fore_color.rgb = COLOR_PRIMARY_RED
    bot_wave.line.fill.background()

    add_slide_badge(slide1, 1)


    # ==================== SLIDE 2: Introduction ====================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2, COLOR_LIGHT_BG)
    add_header(slide2, "Introduction")
    add_slide_badge(slide2, 2)

    # Left content box
    content_box2 = slide2.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(6.8), Inches(4.5))
    tf2 = content_box2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "ShareLife is a web application designed to manage blood donor information efficiently."
    p.font.name = 'Arial'
    p.font.size = Pt(20)
    p.font.color.rgb = COLOR_TEXT_MAIN
    p.line_spacing = 1.3

    p2 = tf2.add_paragraph()
    p2.text = "It helps people find the right donors quickly during emergencies and promotes blood donation for a better and healthier society."
    p2.font.name = 'Arial'
    p2.font.size = Pt(20)
    p2.font.color.rgb = COLOR_TEXT_MAIN
    p2.line_spacing = 1.3
    p2.space_before = Pt(24)

    # Right Illustration Box
    right_card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.2))
    right_card2.fill.solid()
    right_card2.fill.fore_color.rgb = COLOR_CARD_BG
    right_card2.line.color.rgb = COLOR_LIGHT_RED_BG

    # Blood Bag graphic inside right card
    bag = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.65), Inches(2.5), Inches(1.4), Inches(2.2))
    bag.fill.solid()
    bag.fill.fore_color.rgb = COLOR_LIGHT_RED_BG
    bag.line.color.rgb = COLOR_PRIMARY_RED

    bag_inner = slide2.shapes.add_shape(MSO_SHAPE.TEAR, Inches(10.0), Inches(3.0), Inches(0.7), Inches(0.9))
    bag_inner.fill.solid()
    bag_inner.fill.fore_color.rgb = COLOR_PRIMARY_RED
    bag_inner.line.fill.background()
    bag_inner.rotation = 180


    # ==================== SLIDE 3: Problem Statement ====================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3, COLOR_LIGHT_BG)
    add_header(slide3, "Problem Statement")
    add_slide_badge(slide3, 3)

    content_box3 = slide3.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(7.2), Inches(4.5))
    tf3 = content_box3.text_frame
    tf3.word_wrap = True

    problems = [
        "Finding blood donors during emergencies is difficult.",
        "Donor information is often stored manually.",
        "Searching for a matching blood group takes time.",
        "There is no centralized system to manage donor records."
    ]

    for idx, prob in enumerate(problems):
        p = tf3.paragraphs[0] if idx == 0 else tf3.add_paragraph()
        p.text = "•  " + prob
        p.font.name = 'Arial'
        p.font.size = Pt(19)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.line_spacing = 1.2
        if idx > 0:
            p.space_before = Pt(18)

    # Right Side Graphic - Person/Question Mark Illustration Box
    right_card3 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.8), Inches(4.2), Inches(4.2))
    right_card3.fill.solid()
    right_card3.fill.fore_color.rgb = COLOR_CARD_BG
    right_card3.line.color.rgb = COLOR_LIGHT_RED_BG

    q_box = slide3.shapes.add_textbox(Inches(8.5), Inches(2.2), Inches(3.8), Inches(3.4))
    tf_q = q_box.text_frame
    p_q = tf_q.paragraphs[0]
    p_q.alignment = PP_ALIGN.CENTER
    p_q.text = "❓\n🤔\nNeed Blood?"
    p_q.font.name = 'Arial'
    p_q.font.size = Pt(36)
    p_q.font.color.rgb = COLOR_PRIMARY_RED


    # ==================== SLIDE 4: Solution ====================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4, COLOR_LIGHT_BG)
    add_header(slide4, "Solution")
    add_slide_badge(slide4, 4)

    content_box4 = slide4.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(7.0), Inches(4.5))
    tf4 = content_box4.text_frame
    tf4.word_wrap = True

    solutions = [
        "Online donor registration.",
        "Centralized database of donors.",
        "Quick search by blood group.",
        "Easy access to donor information.",
        "Efficient management of donor records."
    ]

    for idx, sol in enumerate(solutions):
        p = tf4.paragraphs[0] if idx == 0 else tf4.add_paragraph()
        p.text = "•  " + sol
        p.font.name = 'Arial'
        p.font.size = Pt(19)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.line_spacing = 1.2
        if idx > 0:
            p.space_before = Pt(14)

    # Right Graphic: Hands holding blood drop card
    right_card4 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.2))
    right_card4.fill.solid()
    right_card4.fill.fore_color.rgb = COLOR_CARD_BG
    right_card4.line.color.rgb = COLOR_LIGHT_RED_BG

    drop4 = slide4.shapes.add_shape(MSO_SHAPE.TEAR, Inches(9.65), Inches(2.6), Inches(1.4), Inches(1.9))
    drop4.fill.solid()
    drop4.fill.fore_color.rgb = COLOR_PRIMARY_RED
    drop4.line.fill.background()
    drop4.rotation = 180

    plus4 = slide4.shapes.add_shape(MSO_SHAPE.CROSS, Inches(10.1), Inches(3.3), Inches(0.5), Inches(0.5))
    plus4.fill.solid()
    plus4.fill.fore_color.rgb = COLOR_WHITE
    plus4.line.fill.background()


    # ==================== SLIDE 5: Objectives ====================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5, COLOR_LIGHT_BG)
    add_header(slide5, "Objectives")
    add_slide_badge(slide5, 5)

    content_box5 = slide5.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(7.0), Inches(4.5))
    tf5 = content_box5.text_frame
    tf5.word_wrap = True

    objectives = [
        "Register blood donors.",
        "Store donor details securely.",
        "Search donors by blood group.",
        "Display all donor records.",
        "Provide a simple and user-friendly system."
    ]

    for idx, obj in enumerate(objectives):
        p = tf5.paragraphs[0] if idx == 0 else tf5.add_paragraph()
        p.text = "🎯  " + obj
        p.font.name = 'Arial'
        p.font.size = Pt(19)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.line_spacing = 1.2
        if idx > 0:
            p.space_before = Pt(14)

    # Right Target Illustration Box
    right_card5 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.2))
    right_card5.fill.solid()
    right_card5.fill.fore_color.rgb = COLOR_CARD_BG
    right_card5.line.color.rgb = COLOR_LIGHT_RED_BG

    target1 = slide5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.1), Inches(2.6), Inches(2.5), Inches(2.5))
    target1.fill.solid()
    target1.fill.fore_color.rgb = COLOR_PRIMARY_RED
    target1.line.fill.background()

    target2 = slide5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.5), Inches(3.0), Inches(1.7), Inches(1.7))
    target2.fill.solid()
    target2.fill.fore_color.rgb = COLOR_WHITE
    target2.line.fill.background()

    target3 = slide5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.9), Inches(3.4), Inches(0.9), Inches(0.9))
    target3.fill.solid()
    target3.fill.fore_color.rgb = COLOR_PRIMARY_RED
    target3.line.fill.background()


    # ==================== SLIDE 6: Features ====================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6, COLOR_LIGHT_BG)
    add_header(slide6, "Features")
    add_slide_badge(slide6, 6)

    features = [
        ("👤+", "Donor\nRegistration"),
        ("🔍", "Search\nDonor"),
        ("👥", "View All\nDonors"),
        ("ℹ️", "About\nPage"),
        ("🛡️", "Secure &\nReliable")
    ]

    card_width = Inches(2.1)
    card_height = Inches(3.8)
    spacing = Inches(0.3)
    start_left = Inches(0.8)
    top_pos = Inches(2.0)

    for i, (icon_str, title_str) in enumerate(features):
        left_pos = start_left + i * (card_width + spacing)
        card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, card_width, card_height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_LIGHT_RED_BG

        # Circle icon background inside card
        icon_circle = slide6.shapes.add_shape(MSO_SHAPE.OVAL, left_pos + Inches(0.4), top_pos + Inches(0.4), Inches(1.3), Inches(1.3))
        icon_circle.fill.solid()
        icon_circle.fill.fore_color.rgb = COLOR_LIGHT_RED_BG
        icon_circle.line.fill.background()

        tf_c = icon_circle.text_frame
        p_c = tf_c.paragraphs[0]
        p_c.alignment = PP_ALIGN.CENTER
        p_c.text = icon_str
        p_c.font.size = Pt(28)

        # Feature Text
        txt_box = slide6.shapes.add_textbox(left_pos + Inches(0.1), top_pos + Inches(2.0), Inches(1.9), Inches(1.5))
        tf_t = txt_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.alignment = PP_ALIGN.CENTER
        p_t.text = title_str
        p_t.font.name = 'Arial'
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN


    # ==================== SLIDE 7: Technology Used ====================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7, COLOR_LIGHT_BG)
    add_header(slide7, "Technology Used")
    add_slide_badge(slide7, 7)

    content_box7 = slide7.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(6.8), Inches(4.5))
    tf7 = content_box7.text_frame
    tf7.word_wrap = True

    techs = [
        "ASP.NET Web Forms",
        "C#",
        "SQL Server (LocalDB)",
        "ADO.NET",
        "HTML & CSS",
        "Visual Studio"
    ]

    for idx, tech in enumerate(techs):
        p = tf7.paragraphs[0] if idx == 0 else tf7.add_paragraph()
        p.text = "✔  " + tech
        p.font.name = 'Arial'
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.line_spacing = 1.2
        if idx > 0:
            p.space_before = Pt(14)

    # Right Side ASP.NET Graphics Card
    right_card7 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(1.8), Inches(4.5), Inches(4.2))
    right_card7.fill.solid()
    right_card7.fill.fore_color.rgb = COLOR_CARD_BG
    right_card7.line.color.rgb = COLOR_LIGHT_RED_BG

    mon_box = slide7.shapes.add_textbox(Inches(8.2), Inches(2.4), Inches(4.1), Inches(3.0))
    tf_m = mon_box.text_frame
    p_m = tf_m.paragraphs[0]
    p_m.alignment = PP_ALIGN.CENTER
    p_m.text = "💻\n\nASP.NET"
    p_m.font.name = 'Arial'
    p_m.font.size = Pt(36)
    p_m.font.bold = True
    p_m.font.color.rgb = COLOR_PRIMARY_RED


    # ==================== SLIDE 8: Database ====================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8, COLOR_LIGHT_BG)
    add_header(slide8, "Database")
    add_slide_badge(slide8, 8)

    db_info_box = slide8.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(7.5), Inches(0.8))
    tf_dbi = db_info_box.text_frame
    p_dbi = tf_dbi.paragraphs[0]
    p_dbi.text = "Database Name: BloodDonorDB    |    Table Name: Donor"
    p_dbi.font.name = 'Arial'
    p_dbi.font.size = Pt(16)
    p_dbi.font.bold = True
    p_dbi.font.color.rgb = COLOR_PRIMARY_RED

    # Table
    rows, cols = 7, 3
    table_shape = slide8.shapes.add_table(rows, cols, Inches(0.8), Inches(2.2), Inches(7.5), Inches(4.0))
    table = table_shape.table

    table.columns[0].width = Inches(2.0)
    table.columns[1].width = Inches(2.2)
    table.columns[2].width = Inches(3.3)

    headers = ["Column Name", "Data Type", "Description"]
    data = [
        ["DonorID", "Int (PK)", "Unique Donor ID"],
        ["Name", "Varchar(100)", "Donor Name"],
        ["Age", "Int", "Donor Age"],
        ["BloodGroup", "Varchar(5)", "Blood Group"],
        ["Mobile", "Varchar(15)", "Mobile Number"],
        ["City", "Varchar(50)", "City"]
    ]

    for col_idx, text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_RED
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.alignment = PP_ALIGN.CENTER
        p.font.name = 'Arial'
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = COLOR_WHITE

    for row_idx, row_data in enumerate(data):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_CARD_BG if row_idx % 2 == 0 else COLOR_LIGHT_BG
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.alignment = PP_ALIGN.LEFT if col_idx > 0 else PP_ALIGN.CENTER
            p.font.name = 'Arial'
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_TEXT_MAIN

    # Right side 3D Database Graphic Box
    right_card8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(1.8), Inches(3.8), Inches(4.4))
    right_card8.fill.solid()
    right_card8.fill.fore_color.rgb = COLOR_CARD_BG
    right_card8.line.color.rgb = COLOR_LIGHT_RED_BG

    db_txt = slide8.shapes.add_textbox(Inches(8.8), Inches(2.6), Inches(3.6), Inches(2.8))
    tf_dbt = db_txt.text_frame
    p_dbt = tf_dbt.paragraphs[0]
    p_dbt.alignment = PP_ALIGN.CENTER
    p_dbt.text = "🗄️\n\nSQL Server\nDatabase"
    p_dbt.font.name = 'Arial'
    p_dbt.font.size = Pt(26)
    p_dbt.font.bold = True
    p_dbt.font.color.rgb = COLOR_PRIMARY_RED


    # ==================== SLIDE 9: Advantages ====================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9, COLOR_LIGHT_BG)
    add_header(slide9, "Advantages")
    add_slide_badge(slide9, 9)

    content_box9 = slide9.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(7.0), Inches(4.5))
    tf9 = content_box9.text_frame
    tf9.word_wrap = True

    advantages = [
        "Easy donor registration.",
        "Fast blood group search.",
        "Centralized database.",
        "User-friendly interface.",
        "Saves time during emergencies."
    ]

    for idx, adv in enumerate(advantages):
        p = tf9.paragraphs[0] if idx == 0 else tf9.add_paragraph()
        p.text = "✔  " + adv
        p.font.name = 'Arial'
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.line_spacing = 1.2
        if idx > 0:
            p.space_before = Pt(14)

    # Right Graphic Card
    right_card9 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.2))
    right_card9.fill.solid()
    right_card9.fill.fore_color.rgb = COLOR_CARD_BG
    right_card9.line.color.rgb = COLOR_LIGHT_RED_BG

    drop9 = slide9.shapes.add_shape(MSO_SHAPE.TEAR, Inches(9.65), Inches(2.6), Inches(1.4), Inches(1.9))
    drop9.fill.solid()
    drop9.fill.fore_color.rgb = COLOR_PRIMARY_RED
    drop9.line.fill.background()
    drop9.rotation = 180


    # ==================== SLIDE 10: Conclusion ====================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10, COLOR_LIGHT_BG)
    add_header(slide10, "Conclusion")
    add_slide_badge(slide10, 10)

    # Content paragraph on the left
    content_box10 = slide10.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.5))
    tf10 = content_box10.text_frame
    tf10.word_wrap = True
    p10 = tf10.paragraphs[0]
    p10.text = "ShareLife – A Blood Donor Management System is a simple and efficient web application developed using ASP.NET Web Forms, C#, ADO.NET, and SQL Server. It enables quick donor registration, efficient donor searching, and easy management of donor records, making it useful during blood emergencies."
    p10.font.name = 'Arial'
    p10.font.size = Pt(19)
    p10.font.color.rgb = COLOR_TEXT_MAIN
    p10.line_spacing = 1.3

    # Right Big Thank You Box
    ty_box = slide10.shapes.add_textbox(Inches(7.8), Inches(2.2), Inches(5.0), Inches(3.5))
    tf_ty = ty_box.text_frame
    tf_ty.word_wrap = True

    p_ty = tf_ty.paragraphs[0]
    p_ty.alignment = PP_ALIGN.CENTER
    p_ty.text = "Thank You!"
    p_ty.font.name = 'Arial'
    p_ty.font.size = Pt(48)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_PRIMARY_RED

    p_q = tf_ty.add_paragraph()
    p_q.alignment = PP_ALIGN.CENTER
    p_q.text = "Questions?"
    p_q.font.name = 'Arial'
    p_q.font.size = Pt(24)
    p_q.font.color.rgb = COLOR_TEXT_MAIN
    p_q.space_before = Pt(14)

    p_heart = tf_ty.add_paragraph()
    p_heart.alignment = PP_ALIGN.CENTER
    p_heart.text = "❤️"
    p_heart.font.size = Pt(36)
    p_heart.space_before = Pt(10)

    output_path = r"d:\ShareLife.net\ShareLife_Presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated PPTX presentation at: {output_path}")

if __name__ == "__main__":
    build_presentation()
