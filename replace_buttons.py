import os
import re

dir_path = r'd:\GrowPark Projects\Stackly_templates\project_27'

old_css_pattern = re.compile(
    r'\.theme-toggle-pill\s*\{.*?\.rtl-btn-style\s*\{.*?\n\s*\}', 
    re.DOTALL
)

new_css = '''.theme-toggle-pill {
            width: 80px;
            height: 32px;
            background: var(--bg-secondary);
            border-radius: 30px;
            position: relative;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10px;
            border: 1px solid var(--border-color);
        }

        .theme-toggle-pill i {
            font-size: 12px;
            z-index: 1;
        }

        .theme-toggle-pill .fa-sun {
            color: #f59e0b;
        }

        .theme-toggle-pill .fa-moon {
            color: #999;
        }

        .theme-toggle-pill .thumb {
            position: absolute;
            top: 2px;
            left: 2px;
            width: 26px;
            height: 26px;
            background: white;
            border-radius: 50%;
            transition: transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            z-index: 2;
            border: 1px solid var(--border-color);
        }

        body.dark-mode .theme-toggle-pill .thumb {
            transform: translateX(48px);
            background: #333;
            border-color: var(--border-color);
        }

        .rtl-btn-style {
            width: 80px;
            height: 32px;
            background: var(--bg-secondary);
            border-radius: 30px;
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            color: var(--text-main);
            transition: all 0.3s ease;
        }'''

old_html_regex = re.compile(
    r'<!-- Buttons left completely untouched -->\s*<a href="login\.html"\s*class="btn btn-outline[^>]+>Login</a>\s*<a href="register\.html"\s*class="btn btn-solid[^>]+>Register</a>',
    re.DOTALL
)

new_html = '''<!-- Buttons standardized to fixed size -->
                <a href="login.html" class="btn btn-solid !w-[80px] !h-[32px] flex items-center justify-center !p-0 !text-[12px] !rounded-[30px]">Login</a>
                <a href="register.html" class="btn btn-solid !w-[80px] !h-[32px] flex items-center justify-center !p-0 !text-[12px] !rounded-[30px]">Register</a>'''


for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Replace CSS
        content = old_css_pattern.sub(new_css, content)
        
        # Replace HTML
        content = old_html_regex.sub(new_html, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filename}')
print('Done')
