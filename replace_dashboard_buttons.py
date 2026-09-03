import os

css_to_add = """
        /* ICONS & BUTTONS */
        .theme-toggle-pill {
            width: 80px; height: 32px; background: var(--bg-secondary); border-radius: 30px; position: relative;
            cursor: pointer; display: flex; align-items: center; justify-content: space-between; padding: 0 10px;
            border: 1px solid var(--border-color);
        }
        .theme-toggle-pill i { font-size: 12px; z-index: 1; }
        .theme-toggle-pill .fa-sun { color: #f59e0b; }
        .theme-toggle-pill .fa-moon { color: #999; }
        .theme-toggle-pill .thumb {
            position: absolute; top: 2px; left: 2px; width: 26px; height: 26px; background: white;
            border-radius: 50%; transition: transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); z-index: 2; border: 1px solid var(--border-color);
        }
        body.dark-mode .theme-toggle-pill .thumb { transform: translateX(48px); background: #333; border-color: var(--border-color); }

        .rtl-btn-style {
            width: 80px; height: 32px; background: var(--bg-secondary); border-radius: 30px;
            border: 1px solid var(--border-color); display: flex; align-items: center; justify-content: center;
            font-size: 10px; font-weight: 600; cursor: pointer; color: var(--text-main); transition: all 0.3s ease;
        }
        .rtl-btn-style:hover { background: var(--accent-color); color: #fff; border-color: var(--accent-color); }

        .icon-btn {"""

html_to_replace = """                <button class="icon-btn hidden sm:flex" id="rtl-toggle"><i class="fas fa-align-right"></i></button>
                <button class="icon-btn" id="theme-toggle"><i class="fas fa-moon"></i></button>"""

html_new = """                <button id="rtl-toggle" class="rtl-btn-style" title="Toggle LTR/RTL">LTR</button>
                <div id="theme-toggle" class="theme-toggle-pill" title="Toggle Dark Mode">
                    <i class="fas fa-sun"></i><i class="fas fa-moon"></i>
                    <div class="thumb"></div>
                </div>"""

js_theme_old = """        function applyTheme(isDark) {
            document.body.classList.toggle('dark-mode', isDark);
            document.getElementById('theme-toggle').querySelector('i').className = isDark ? 'fas fa-sun' : 'fas fa-moon';
        }"""

js_theme_new = """        function applyTheme(isDark) {
            document.body.classList.toggle('dark-mode', isDark);
        }"""

js_rtl_old = """        document.getElementById('rtl-toggle').addEventListener('click', () => {
            const isRTL = document.documentElement.dir === 'rtl';
            document.documentElement.dir = isRTL ? 'ltr' : 'rtl';
            localStorage.setItem('dir', isRTL ? 'ltr' : 'rtl');
        });"""

js_rtl_new = """        document.getElementById('rtl-toggle').addEventListener('click', () => {
            const isRTL = document.documentElement.dir === 'rtl';
            document.documentElement.dir = isRTL ? 'ltr' : 'rtl';
            localStorage.setItem('dir', isRTL ? 'ltr' : 'rtl');
            document.getElementById('rtl-toggle').innerText = isRTL ? 'LTR' : 'RTL';
        });"""

js_rtl_init_old = """        if (localStorage.getItem('dir') === 'rtl') document.documentElement.dir = 'rtl';"""
js_rtl_init_new = """        if (localStorage.getItem('dir') === 'rtl') {
            document.documentElement.dir = 'rtl';
            document.getElementById('rtl-toggle').innerText = 'RTL';
        }"""

for file in ["user.html", "admin.html"]:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("        /* ICONS & BUTTONS */\n        .icon-btn {", css_to_add)
    content = content.replace(html_to_replace, html_new)
    content = content.replace(js_theme_old, js_theme_new)
    content = content.replace(js_rtl_old, js_rtl_new)
    content = content.replace(js_rtl_init_old, js_rtl_init_new)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")
