from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Complete synchronized resume dataset directly from the CV artifact
CV_DATA = {
    "name": "GURU PRASAD K",
    "title": "DevOps / AWS Cloud Engineer",
    "location": "Bangalore, India",
    "email": "guru2024g3@outlook.com",
    "linkedin": "linkedin.com/in/k-guru-prasad",
    "phone": "+91-9449530539",
    "summary": "DevOps/AWS Cloud Engineer with hands-on experience in cloud infrastructure monitoring, CI/CD automation, containerization, and AWS services. Strong practical exposure to AWS, Jenkins, Docker, Linux, and CloudWatch. Passionate about automation, system reliability, and cloud operations AI-driven automation (Gemini, Copilot) and Low-Code/No-Code workflows (n8n, Power Automate) to streamline operations and enhance productivity.",
    "skills": [
        "AWS (EC2, EKS, S3, VPC, RDS, IAM, Auto Scaling, Route53, CloudWatch, CLI)", "Azure", 
        "Jenkins", "GitHub Webhooks", "GitLab CI/CD", "Docker", "Helm", "Prometheus", "Grafana", 
        "Python", "Bash", "Ansible", "Git", "GitHub", "GitLab", "Linux", "Windows", "RHEL", 
        "SonarQube", "Kubernetes", "Terraform", "n8n", "Microsoft Power Automate", "GitHub Copilot", "Google Gemini (GenAI)"
    ],
    "experience": [
        {
            "role": "Technical Support Representative-L1 (DevOps)",
            "company": "Joules to Watts (J2W)",
            "period": "Apr 2024 - Present",
            "bullets": [
                "Built, supported, and maintained CI/CD pipelines using Jenkins to automate application build, test, and deployment workflows.",
                "Integrated GitHub/GitLab repositories with Jenkins for continuous integration using webhooks.",
                "Implemented pipeline stages for code checkout, build, unit testing, static code analysis, and deployment.",
                "Integrated SonarQube with Jenkins pipelines to perform static code analysis and enforce quality gates.",
                "Created and maintained Docker files, built Docker images, and pushed images to container registries.",
                "Assisted in deploying containerized applications on Kubernetes (basic exposure) and validating deployments.",
                "Used Terraform (Infrastructure as Code) to provision and manage AWS and Azure cloud resources in a repeatable manner.",
                "Monitored AWS and Azure infrastructure using AWS CloudWatch and Azure Monitor.",
                "Centralized application and system logs using CloudWatch Log Groups and Azure Log Analytics.",
                "Configured CloudWatch Alarms and Azure Alerts to monitor CPU, memory, disk, and application errors.",
                "Automated alert notifications using Amazon SNS and Azure alert action groups (email notifications).",
                "Supported basic automation using AWS Lambda and Azure automation concepts for operational tasks.",
                "Managed cloud security and access control using AWS IAM and Azure Active Directory (AAD).",
                "Archived logs and backups to Amazon S3 and Azure Storage Accounts for long-term retention.",
                "Collaborated with development and QA teams to troubleshoot CI/CD pipeline failures, deployment issues, and environment problems.",
                "Followed DevOps best practices for automation, reliability, monitoring, and continuous improvement.",
                "Implemented n8n and Power Automate to trigger operational alerts and automate repetitive ticketing tasks."
            ]
        },
        {
            "role": "Consultant - MFG IT Engineer",
            "company": "Newwave Computing Limited",
            "period": "May 2024 - Apr 2025",
            "bullets": [
                "Managed GxP equipment installation, qualification, and validation using ValGenesis.",
                "Supported GxP systems, laboratory and manufacturing applications.",
                "Performed backup and restore, infrastructure support, and preventive maintenance.",
                "Prepared and executed IQ/OQ and CSV documentation.",
                "Supported Windows Server (2003-2016) and handled access reviews and compliance.",
                "Troubleshot manufacturing equipment such as HMI, IPC, and automation systems."
            ]
        },
        {
            "role": "Consultant - IT Desktop Support Engineer",
            "company": "Newwave Computing Limited",
            "period": "Jun 2022 - May 2024",
            "bullets": [
                "Troubleshot hardware and software issues across Windows environments.",
                "Supported Office 365, DNS setup, printers, scanners, and remote access.",
                "Managed system configurations, user access, and asset management.",
                "Provided on-site and remote IT support to end users."
            ]
        }
    ],
    "projects": [
        {
            "title": "CI/CD Pipeline Automation",
            "subtitle": "Accelerated Web App Development with Jenkins Pipeline Triggered by GitHub Webhook Integration",
            "bullets": [
                "The Jenkins pipeline will be triggered automatically by GitHub Webhook Integration when changes are made to the code repository.",
                "Built Jenkins pipelines triggered by GitHub Webhooks to automate build, test, and deployment stages.",
                "Integrated SonarQube for static code analysis.",
                "Utilized GitHub Copilot to optimize Groovy scripts for Jenkins pipelines, reducing pipeline failure rates by 15%."
            ]
        },
        {
            "title": "2048 Game Deployment on AWS",
            "subtitle": "Containerized Infrastructure Lifecycle",
            "bullets": [
                "Containerized a 2048 web application using Docker.",
                "Deployed application stack smoothly on AWS EC2 with EBS storage volumes.",
                "Ensured application accessibility, uptime stability, and performance optimization."
            ]
        }
    ],
    "education": {
        "degree": "BCA - Bachelor of Computer Applications",
        "institution": "St. Vincent Pallotti College"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} | DevOps Infrastructure Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">

    <header class="bg-slate-900 text-white py-16 px-6 shadow-xl border-b-4 border-emerald-500">
        <div class="max-w-4xl mx-auto flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
            <div>
                <h1 class="text-4xl font-extrabold tracking-tight">{{ data.name }}</h1>
                <p class="text-xl text-emerald-400 mt-2 font-mono font-medium">[ {{ data.title }} ]</p>
                <p class="text-sm text-slate-400 mt-1 flex items-center gap-1">📍 {{ data.location }}</p>
            </div>
            <div class="text-sm font-mono text-slate-300 space-y-2 bg-slate-950/50 p-4 rounded-lg border border-slate-800 w-full md:w-auto">
                <p>📧 <a href="mailto:{{ data.email }}" class="hover:text-emerald-400 transition-colors">{{ data.email }}</a></p>
                <p>📱 {{ data.phone }}</p>
                <p>🔗 <a href="https://{{ data.linkedin }}" target="_blank" class="hover:text-emerald-400 transition-colors">{{ data.linkedin }}</a></p>
            </div>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-12 space-y-12">
        
        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 border-b-2 border-emerald-500 pb-2 mb-4">About Me</h2>
            <p class="text-slate-600 leading-relaxed text-justify">{{ data.summary }}</p>
        </section>

        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 border-b-2 border-emerald-500 pb-2 mb-4">Technical Skills Inventory</h2>
            <div class="flex flex-wrap gap-2">
                {% for skill in data.skills %}
                <span class="bg-slate-900 text-slate-100 text-xs px-3 py-1.5 rounded font-mono shadow-sm transition-transform hover:scale-105">
                    {{ skill }}
                </span>
                {% endfor %}
            </div>
        </section>

        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 border-b-2 border-emerald-500 pb-2 mb-6">Professional Experience</h2>
            <div class="space-y-8">
                {% for exp in data.experience %}
                <div class="relative pl-6 border-l-2 border-slate-200 hover:border-emerald-400 transition-colors">
                    <div class="absolute -left-[6px] top-1.5 w-2.5 h-2.5 bg-slate-400 rounded-full border border-white"></div>
                    <div class="flex flex-col sm:flex-row sm:justify-between items-start sm:items-center mb-2">
                        <h3 class="text-lg font-bold text-slate-900">{{ exp.role }}</h3>
                        <span class="text-xs font-mono font-semibold bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full border border-emerald-200 mt-1 sm:mt-0">{{ exp.period }}</span>
                    </div>
                    <p class="text-sm font-semibold text-slate-500 mb-4 font-mono">{{ exp.company }}</p>
                    <ul class="list-disc pl-5 space-y-2 text-sm text-slate-600">
                        {% for bullet in exp.bullets %}
                        <li class="leading-relaxed">{{ bullet }}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endfor %}
            </div>
        </section>

        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 border-b-2 border-emerald-500 pb-2 mb-6">Technical Engineering Projects</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                {% for proj in data.projects %}
                <div class="bg-slate-50 p-5 rounded-lg border border-slate-200 shadow-inner flex flex-col justify-between">
                    <div>
                        <h3 class="text-md font-bold text-slate-900 mb-1 flex items-center gap-1.5 text-emerald-700">🛠️ {{ proj.title }}</h3>
                        <p class="text-xs italic text-slate-500 mb-3 font-mono leading-tight">{{ proj.subtitle }}</p>
                        <ul class="space-y-1.5 text-xs text-slate-600 list-none">
                            {% for bullet in proj.bullets %}
                            <li class="relative pl-3.5"><span class="absolute left-0 text-emerald-500">▹</span>{{ bullet }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>

        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 border-b-2 border-emerald-500 pb-2 mb-4">Education</h2>
            <div class="flex justify-between items-center font-mono text-sm">
                <div>
                    <h3 class="font-bold text-slate-900">{{ data.education.degree }}</h3>
                    <p class="text-slate-500 text-xs">{{ data.education.institution }}</p>
                </div>
            </div>
        </section>

        <section class="bg-slate-950 text-slate-200 p-6 rounded-xl shadow-2xl font-mono text-sm border border-slate-800">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
                <div class="flex items-center space-x-2">
                    <span class="w-3 h-3 bg-red-500 rounded-full inline-block"></span>
                    <span class="w-3 h-3 bg-yellow-500 rounded-full inline-block"></span>
                    <span class="w-3 h-3 bg-green-500 rounded-full inline-block"></span>
                    <span class="text-xs text-slate-500 pl-2">guest@guru-cloud-shell:~</span>
                </div>
                <span class="text-xs text-emerald-500/70 font-semibold animate-pulse">● Live Engine</span>
            </div>
            <div id="terminal-output" class="space-y-2 max-h-64 overflow-y-auto mb-4 scrollbar-thin scrollbar-thumb-slate-800">
                <p class="text-slate-400">Welcome to Guru Prasad's interactive shell interface. Type <span class="text-emerald-400 font-bold">help</span> to explore cloud portfolio objects.</p>
            </div>
            <div class="flex items-center border-t border-slate-900 pt-2">
                <span class="text-emerald-400 font-bold mr-2">guru-nodes$</span>
                <input type="text" id="terminal-input" class="bg-transparent focus:outline-none text-slate-100 flex-grow caret-emerald-400" autofocus placeholder="Run terminal query...">
            </div>
        </section>

    </main>

    <footer class="text-center py-8 text-xs font-mono text-slate-400">
        &copy; 2026 {{ data.name }} • Stack: Python (Flask) & Tailwind CSS Container Engine
    </footer>

    <script>
        const input = document.getElementById('terminal-input');
        const output = document.getElementById('terminal-output');

        input.addEventListener('keydown', async function(e) {
            if (e.key === 'Enter') {
                const command = this.value.trim();
                if (!command) return;

                const lowerCommand = command.toLowerCase();

                // 1. If clear is typed, completely empty previous inputs/logs instantly from the screen
                if (lowerCommand === 'clear') {
                    output.innerHTML = ''; 
                    this.value = '';
                } else {
                    // Otherwise echo normal input strings
                    output.innerHTML += `<p class="text-slate-400"><span class="text-emerald-400 font-bold">guru-nodes$</span> ${command}</p>`;
                    this.value = '';
                }

                // 2. Fetch from backend to show results (including the 'clear' response)
                const response = await fetch('/terminal', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ command: command })
                });
                const data = await response.json();
                
                output.innerHTML += `<p class="text-slate-300 whitespace-pre-line leading-relaxed">${data.result}</p>`;
                output.scrollTop = output.scrollHeight;
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, data=CV_DATA)

@app.route('/terminal', methods=['POST'])
def terminal_command():
    req_data = request.get_json()
    command = req_data.get('command', '').strip().lower()

    if command == 'help':
        result = (
            "Available infrastructure objects:\n"
            "  - <span class='text-cyan-400 font-bold'>metrics</span>    : Show metrics optimized with AI coding models\n"
            "  - <span class='text-cyan-400 font-bold'>pipelines</span>  : List standard automation tasks in current tenancy\n"
            "  - <span class='text-cyan-400 font-bold'>cloud-ops</span>  : Output telemetry and log retention capabilities\n"
            "  - <span class='text-cyan-400 font-bold'>clear</span>     : Flush display buffer logs"
        )
    elif command == 'metrics':
        result = "🚀 <span class='text-emerald-400 font-bold'>Script Optimization Metric:</span> Groovy configuration logic refactored via GitHub Copilot integration, successfully reducing execution runtime pipeline failures by 15%."
    elif command == 'pipelines':
        result = "🔀 <span class='text-emerald-400 font-bold'>Active Toolchain Stack:</span> Jenkins Continuous Integration Pipelines configured via explicit GitHub/GitLab Webhook rules. Multi-stage analysis utilizes SonarQube Quality Gates."
    elif command == 'cloud-ops':
        result = "☁️ <span class='text-emerald-400 font-bold'>Logging/Telemetry Infrastructure:</span> Configured multi-cloud monitoring (AWS CloudWatch + Azure Monitor). Backups and system log histories are routed to storage pools (S3 + Azure Storage Accounts) for long-term audit preservation."
    elif command == 'clear': 
        result = "Operational display cleared."
    else:
        result = f"bash: command not found: '{command}'. Execute 'help' to get structural object targets."

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

0
0
