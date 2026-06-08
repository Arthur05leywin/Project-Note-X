import os
import re
from bs4 import BeautifulSoup

file_path = 'c:/Users/sayan/Downloads/BIOCHEM_MODULE_5/module05_nucleotide_metabolism.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_old = "@media(max-width:600px){.hero{padding:2rem 1rem;}.content{padding:0 1rem 2rem;}.toc{margin:1rem;}.flow-h{flex-direction:column;align-items:stretch;}.arrow{display:none;}}"
css_new = """@media(max-width:768px){
  .hero{padding:2rem 1rem;}
  .content{padding:0 1rem 2rem;}
  .toc{margin:1rem 0; width:auto; display: block;}
  .flow-h, .two-col, .atom-grid {display:flex !important; flex-direction:column !important; align-items:stretch !important;}
  .flow-box {min-width: unset !important; max-width: 100% !important; margin-left: 0 !important; margin-right: 0 !important; border-right: 1px solid var(--border) !important;}
  .arrow{display:block !important; text-align:center !important; transform:rotate(90deg) !important; margin: 6px 0 !important;}
  .arrow-down{max-width:100% !important;}
}

@media print {
  :root {
    --bg: #ffffff;
    --surface: #ffffff;
    --surface2: #ffffff;
    --surface3: #ffffff;
    --text: #000000;
    --text2: #000000;
    --text3: #000000;
    --border: #cccccc;
    --border2: #cccccc;
    --accent: #000000;
    --accent2: #000000;
    --accent3: #000000;
    --gold: #000000;
    --rose: #000000;
    --purple: #000000;
    --blue: #000000;
    --green: #000000;
    --orange: #000000;
  }
  body, .hero, .content, .footer { background: #ffffff !important; color: #000000 !important; font-size: 11pt; }
  * { color: #000000 !important; background: transparent !important; box-shadow: none !important; text-shadow: none !important; }
  .hero { background: none !important; border-bottom: 2px solid #000 !important; padding: 1rem 0; }
  .hero::before, .hero::after { display: none !important; }
  .toc, .top-btn, .progress-bar { display: none !important; }
  .card, .clinical-box, .mnemonic-box, .flowchart, details, .atom-card, table { page-break-inside: avoid !important; }
  .section-num { background: none !important; border: 2px solid #000; color: #000 !important; }
  a { text-decoration: none !important; color: #000000 !important; }
  details { border: 1px solid #000 !important; }
  details[open]>summary::before { display: none !important; }
  summary::before { display: none !important; }
  .viva-ans { display: block !important; border-top: 1px solid #ccc !important; }
  /* Expanding details fully in print */
  details::details-content { display: block !important; }
}"""

if css_old in html:
    html = html.replace(css_old, css_new)
else:
    # Fallback to regex replacement
    html = re.sub(r'@media\s*\(\s*max-width:\s*600px\s*\)\s*\{[^}]+\}', css_new, html)

# If it wasn't there at all, append it
if css_new not in html:
    html = html.replace('</style>', css_new + '\n</style>')

soup = BeautifulSoup(html, 'html.parser')

# 2. Add Missing Drugs to Drug Table
s8 = soup.find(id='s8')
if s8:
    table = s8.find('table')
    if table:
        new_row1 = BeautifulSoup('''<tr>
        <td>Mycophenolate & Ribavirin <span class="drug-tag">Immunosuppressant</span></td>
        <td>Purine precursors</td>
        <td>IMP Dehydrogenase</td>
        <td>Inhibits conversion of IMP to Xanthosine-5-P → ↓ GMP synthesis in rapidly dividing B/T cells</td>
        <td>Organ transplant, Hepatitis C</td>
      </tr>''', 'html.parser').tr
        new_row2 = BeautifulSoup('''<tr>
        <td>Hydroxyurea <span class="drug-tag">Anticancer</span></td>
        <td>-</td>
        <td>Ribonucleotide Reductase (RNR)</td>
        <td>Inhibits conversion of ribonucleotides to deoxyribonucleotides → ↓ DNA synthesis</td>
        <td>Melanoma, Sickle Cell (↑ HbF)</td>
      </tr>''', 'html.parser').tr
        table.append(new_row1)
        table.append(new_row2)

# 3. Transform .eq-box into interactive details
for eq_box in soup.find_all('div', class_='eq-box'):
    eq_title = eq_box.find('div', class_='eq-title')
    eq_statement = eq_box.find('div', class_='eq-statement')
    eq_answer = eq_box.find('div', class_='eq-answer')
    
    if eq_title and eq_statement and eq_answer:
        q_text = eq_statement.text.strip('\'"')
        year_match = re.search(r'\[(.*?)\]', eq_title.text)
        year_text = year_match.group(1) if year_match else "EQ"
        
        details = soup.new_tag('details')
        summary = soup.new_tag('summary')
        
        span_q = soup.new_tag('span', attrs={'class': 'viva-q'})
        span_q.string = q_text
        span_y = soup.new_tag('span', attrs={'class': 'viva-year'})
        span_y.string = year_text
        
        summary.append(span_q)
        summary.append(span_y)
        
        viva_ans = soup.new_tag('div', attrs={'class': 'viva-ans'})
        for child in eq_answer.contents:
            viva_ans.append(child)
            
        details.append(summary)
        details.append(viva_ans)
        
        eq_box.replace_with(details)

# 4. Transform High-Yield Quickfire Table into active-recall accordions
for card in soup.find_all('div', class_='card'):
    title = card.find('div', class_='card-title')
    if title and 'High-Yield Quickfire' in title.text:
       table = card.find('table')
       if table:
           viva_section = soup.new_tag('div', attrs={'class': 'viva-section', 'style': 'margin-top:1.5rem;'})
           
           title_bar = soup.new_tag('div', attrs={'class': 'viva-title-bar'})
           title_bar.string = "🔥 Exam Day High-Yield Quickfire — Module 05"
           viva_section.append(title_bar)
           
           for tr in table.find_all('tr')[1:]:
               tds = tr.find_all('td')
               if len(tds) == 2:
                   details = soup.new_tag('details')
                   summary = soup.new_tag('summary')
                   span_q = soup.new_tag('span', attrs={'class': 'viva-q'})
                   span_q.string = tds[0].text
                   summary.append(span_q)
                   
                   ans = soup.new_tag('div', attrs={'class': 'viva-ans'})
                   p = soup.new_tag('p')
                   p.string = tds[1].text
                   ans.append(p)
                   
                   details.append(summary)
                   details.append(ans)
                   viva_section.append(details)
           
           card.replace_with(viva_section)

# 5. Remove any leftover inline min-width from flow-box globally
for flow_box in soup.find_all('div', class_='flow-box'):
    if flow_box.has_attr('style'):
        style = flow_box['style']
        style = re.sub(r'min-width:\s*\d+px;?', '', style)
        if style.strip() == '':
            del flow_box['style']
        else:
            flow_box['style'] = style

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
