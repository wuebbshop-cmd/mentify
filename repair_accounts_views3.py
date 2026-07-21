from pathlib import Path

path = Path(r'c:\Users\adm\.vscode\Products\EduAI\accounts\views.py')
text = path.read_text(encoding='utf-8')

# fix malformed newline after welcome message
text = text.replace(
    'messages.success(request, f"Welcome to Mentify, {user.first_name}!")            return redirect(user.get_dashboard_url())\n',
    'messages.success(request, f"Welcome to Mentify, {user.first_name}!")\n            return redirect(user.get_dashboard_url())\n',
)

# fix duplicate login_view signature
text = text.replace('def login_view(request):def login_view(request):\n', 'def login_view(request):\n', 1)

path.write_text(text, encoding='utf-8')
print('patched accounts/views.py')
print('login_view count', text.count('def login_view(request):'))
print('sample', text[text.find('def login_view(request):'):text.find('def login_view(request):')+120])
