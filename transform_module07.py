import os
import re
from bs4 import BeautifulSoup

base_dir = r'c:\Users\sayan\Downloads\biochem Note X\modules\module-07'
files = [
    'module07_biological_oxidation.html',
    'module07_biological_oxidation_X.html'
]

# Logo HTML snippet for MODERN layout
MODERN_LOGO_HTML = '''      <div class="brand-container" style="margin-bottom:20px;">
        <img src="../../Caffeine%20%26%20Cadaver.jpg" alt="Caffeine &amp; Cadaver Logo" class="brand-logo">
      </div>
'''

for filename in files:
    file_path = os.path.join(base_dir, filename)
    print(f'Processing {file_path}...')
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Clean up old stylesheets
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'MBBS PYQ_master_style.css' in href or 'wbuhs_master_style.css' in href:
            link.decompose()
            
    # Add back the correct wbuhs_master_style.css link
    if not soup.find('link', href='wbuhs_master_style.css'):
        new_link = soup.new_tag('link', rel='stylesheet', href='wbuhs_master_style.css')
        if soup.head:
            soup.head.append(new_link)

    # 2. Inject Logo if missing
    hero = soup.find('div', class_='hero')
    if hero and not hero.find('div', class_='brand-container'):
        logo_soup = BeautifulSoup(MODERN_LOGO_HTML, 'html.parser')
        hero.insert(0, logo_soup)

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
               title_bar.string = "🔥 Exam Day High-Yield Quickfire — Module 07"
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
    
    print(f'Finished {filename}')

