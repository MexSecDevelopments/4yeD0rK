# generador_dorks.py

def generate_dorks_for_category(category, domain, mode):
    dorks = []
    
    if category == "Footholds":
        keywords = ["admin", "login", "install", "setup", "config", "cmd", "shell", "backdoor", "vulnerable", "debug"]
        operators = ["site:", "inurl:", "intitle:", "filetype:", "ext:", "intext:"]
        filetypes = ["php", "asp", "jsp", "html", "js", "txt", "sql", "config", "xml", "bak"]

    elif category == "Files containing usernames":
        keywords = ["username", "user", "user_list", "usernames", "members", "accounts", "users"]
        operators = ["filetype:", "intitle:", "inurl:", "ext:"]
        filetypes = ["txt", "csv", "sql", "xml", "log", "conf", "ini", "dat", "bak"]

    elif category == "Sensitive Directories":
        keywords = ["admin", "backup", "db", "database", "config", "secure", "private", "cgi-bin", "logs", "wp-content"]
        operators = ["intitle:", "inurl:", "site:"]
        directories = ["/admin/", "/backup/", "/db/", "/config/", "/private/", "/cgi-bin/", "/logs/", "/wp-content/", "/secure/", "/database/"]

    elif category == "Web Server Detection":
        keywords = ["apache", "nginx", "iis", "server", "tomcat", "httpd", "webserver", "status", "version", "powered by"]
        operators = ["intitle:", "inurl:", "ext:", "intext:"]
        filetypes = ["php", "asp", "jsp", "html", "txt", "log", "config", "xml", "bak"]

    elif category == "Vulnerable Files":
        keywords = ["vulnerable", "exploit", "old_version", "unpatched", "deprecated", "insecure", "weakness", "security_bug", "flaw", "security_hole"]
        operators = ["filetype:", "inurl:", "intitle:", "ext:"]
        filetypes = ["php", "asp", "jsp", "cgi", "html", "js", "txt", "sql", "config", "xml", "bak", "log"]

    elif category == "Vulnerable Servers":
        keywords = ["vulnerable", "exploit", "unpatched", "security_bug", "flaw", "security_hole", "misconfiguration", "default_password", "open_port", "exposed_admin"]
        operators = ["intitle:", "inurl:", "site:", "ext:", "intext:"]
        server_info = ["server_status", "server_info", "env_vars", "phpinfo", "test_page", "setup", "config", "admin"]

    elif category == "Error Messages":
        keywords = ["error", "exception", "failed", "invalid", "cannot", "unable", "warning", "not found", "access denied", "syntax error", "SQL syntax"]
        operators = ["intext:", "inurl:", "filetype:", "site:", "ext:"]
        filetypes = ["php", "asp", "jsp", "html", "log", "txt", "config", "xml", "sql", "js"]

    elif category == "Files containing juicy info":
        keywords = ["confidential", "private", "secret", "password", "login", "usernames", "credentials", "accounts", "config", "database"]
        operators = ["filetype:", "intext:", "inurl:", "site:", "ext:"]
        filetypes = ["pdf", "doc", "docx", "xls", "xlsx", "txt", "csv", "sql", "xml", "log", "bak", "config"]

    elif category == "Files containing passwords":
        keywords = ["password", "passwd", "pwd", "credentials", "auth", "authentication", "login", "user_pass", "db_pass", "access"]
        operators = ["filetype:", "intext:", "inurl:", "ext:"]
        filetypes = ["txt", "csv", "sql", "xml", "log", "config", "ini", "dat", "bak"]

    elif category == "Sensitive online shopping info":
        keywords = ["order", "credit card", "purchase", "invoice", "receipt", "customer", "cart", "transaction", "billing", "account"]
        operators = ["filetype:", "intext:", "inurl:", "ext:"]
        filetypes = ["pdf", "doc", "docx", "xls", "xlsx", "csv", "sql", "xml", "log", "txt", "bak"]

    elif category == "Network or Vulnerability Data":
        keywords = ["network", "vulnerability", "scan", "report", "security", "firewall", "router", "switch", "config", "log", "intrusion", "NIDS", "HIDS", "IPS"]
        operators = ["filetype:", "intext:", "inurl:", "ext:"]
        filetypes = ["pdf", "doc", "docx", "xls", "xlsx", "csv", "txt", "log", "xml", "sql", "config", "bak"]

    elif category == "Pages containing login portals":
        keywords = ["login", "signin", "admin", "portal", "username", "password", "authenticate", "logon", "access", "account"]
        operators = ["inurl:", "intitle:", "site:"]
        directories = ["/login", "/admin", "/portal", "/signin", "/auth", "/access", "/user/login", "/administration", "/secure", "/userportal"]

    elif category == "Advisories and Vulnerabilities":
        keywords = ["advisory", "vulnerability", "CVE", "exploit", "patch", "update", "security bulletin", "risk", "flaw", "security advisory"]
        operators = ["filetype:", "intext:", "inurl:", "ext:", "site:"]
        filetypes = ["pdf", "doc", "docx", "txt", "html", "log", "xml", "csv"]

    # Limitando el número de dorks según el modo
    if mode == "Light":
        dork_limit = 10
    elif mode == "Normal":
        dork_limit = 20
    elif mode == "Diablo":
        dork_limit = float('inf')  # Sin límite práctico

    dork_count = 0
    for keyword in keywords:
        for operator in operators:
            if operator in ["filetype:", "ext:"]:
                for filetype in filetypes:
                    if dork_count >= dork_limit:
                        return dorks
                    dork = f"{operator}{filetype} \"{keyword}\""
                    dorks.append(f"site:{domain} {dork}")
                    dork_count += 1

    for keyword in keywords:
        for operator in operators:
            if operator not in ["filetype:", "ext:"]:
                if category in ["Sensitive Directories", "Pages containing login portals"] and 'directories' in locals():
                    for directory in directories:
                        dork = f"{operator}\"{directory}\""
                        dorks.append(f"site:{domain} {dork}")
                else:
                    dork = f"{operator}\"{keyword}\""
                    dorks.append(f"site:{domain} {dork}")

    return dorks

