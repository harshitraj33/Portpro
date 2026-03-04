from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe


# Extend Django's default admin site to add custom CSS
class MyAdminSite(AdminSite):
    """Custom Admin Site with theme styling added to default admin"""
    
    def each_context(self, request):
        context = super().each_context(request)
        # Add custom CSS to every admin page
        css = '''
            <style>
                /* Import Orbitron Font */
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
                
                :root {
                    --poi-black: #0a0a0a;
                    --poi-dark: #0d1117;
                    --poi-blue: #00a8e8;
                    --poi-white: #ffffff;
                    --poi-gray: #1a1a1a;
                    --poi-border: #333;
                }
                
                /* Body & Base Styles */
                body {
                    background-color: var(--poi-black) !important;
                    color: #e5e7eb !important;
                    font-family: 'Orbitron', 'Courier New', monospace !important;
                }
                
                /* Header */
                #header {
                    background: var(--poi-dark) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                #header a.brand {
                    color: var(--poi-blue) !important;
                    text-shadow: 0 0 5px var(--poi-blue) !important;
                }
                
                /* Sidebar */
                #nav-sidebar {
                    background: var(--poi-dark) !important;
                    border-right: 1px solid var(--poi-border) !important;
                }
                
                #nav-sidebar a {
                    color: #9ca3af !important;
                }
                
                #nav-sidebar a:hover {
                    background-color: #1a1a1a !important;
                    color: var(--poi-blue) !important;
                }
                
                #nav-sidebar a.selected {
                    background-color: rgba(0, 168, 232, 0.1) !important;
                    color: var(--poi-blue) !important;
                    border-left: 2px solid var(--poi-blue) !important;
                }
                
                /* Module / Card Styles */
                .module {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                    border-radius: 8px !important;
                    box-shadow: 0 0 5px rgba(0, 168, 232, 0.1) !important;
                }
                
                .module h2, .module h3 {
                    background: var(--poi-gray) !important;
                    color: var(--poi-blue) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                /* Table Styles */
                .results table {
                    background: var(--poi-dark) !important;
                }
                
                .results th {
                    background: var(--poi-gray) !important;
                    color: var(--poi-blue) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                .results td {
                    border-bottom: 1px solid var(--poi-border) !important;
                    color: #e5e7eb !important;
                }
                
                .results tr:hover {
                    background: rgba(0, 168, 232, 0.05) !important;
                }
                
                /* Form Styles */
                input[type="text"],
                input[type="password"],
                input[type="email"],
                input[type="url"],
                input[type="number"],
                textarea,
                select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                    border-radius: 4px !important;
                }
                
                input:focus, textarea:focus, select:focus {
                    border-color: var(--poi-blue) !important;
                    box-shadow: 0 0 5px var(--poi-blue) !important;
                    outline: none !important;
                }
                
                /* Labels */
                label {
                    color: var(--poi-blue) !important;
                }
                
                /* Buttons */
                .button, input[type="submit"], .submit-row input {
                    background: transparent !important;
                    border: 1px solid var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                    border-radius: 4px !important;
                }
                
                .button:hover, input[type="submit"]:hover, .submit-row input:hover {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                    box-shadow: 0 0 15px var(--poi-blue) !important;
                }
                
                .button.default, input[type="submit"].default {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                }
                
                /* Links */
                a {
                    color: var(--poi-blue) !important;
                }
                
                a:hover {
                    color: #00c8ff !important;
                }
                
                /* Breadcrumbs */
                .breadcrumbs {
                    background: var(--poi-gray) !important;
                    color: #9ca3af !important;
                }
                
                /* Pagination */
                .paginator {
                    background: var(--poi-gray) !important;
                    border-top: 1px solid var(--poi-border) !important;
                }
                
                .paginator a, .paginator span {
                    border: 1px solid var(--poi-border) !important;
                    color: #9ca3af !important;
                }
                
                .paginator a:hover {
                    border-color: var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Filter Sidebar */
                #changelist-filter {
                    background: var(--poi-gray) !important;
                    border-left: 1px solid var(--poi-border) !important;
                }
                
                #changelist-filter h3 {
                    color: var(--poi-blue) !important;
                }
                
                #changelist-filter li a {
                    color: #9ca3af !important;
                }
                
                #changelist-filter li.selected a {
                    color: var(--poi-blue) !important;
                }
                
                /* Toolbar */
                #toolbar {
                    background: var(--poi-gray) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                #searchbar {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Actions */
                .actions {
                    background: var(--poi-gray) !important;
                    border-bottom: 1px solid var(--poi-border) !important;
                }
                
                .actions select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Messages */
                .messagelist .success {
                    background: rgba(34, 197, 94, 0.1) !important;
                    border: 1px solid #22c55e !important;
                    color: #22c55e !important;
                }
                
                .messagelist .error {
                    background: rgba(239, 68, 68, 0.1) !important;
                    border: 1px solid #ef4444 !important;
                    color: #ef4444 !important;
                }
                
                /* Delete confirmation */
                .delete-confirmation {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                /* Date hierarchy */
                .date-hierarchy {
                    background: var(--poi-gray) !important;
                }
                
                /* Login page specific */
                .login #header {
                    display: none !important;
                }
                
                .login #container {
                    background: var(--poi-black) !important;
                }
                
                /* Selector */
                select {
                    background: var(--poi-black) !important;
                    border: 1px solid var(--poi-border) !important;
                    color: var(--poi-blue) !important;
                }
                
                /* Checkbox */
                input[type="checkbox"] {
                    accent-color: var(--poi-blue) !important;
                }
                
                /* Calendar & DateTime */
                .calendarbox, .clockbox {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                .calendarbox a, .clockbox a {
                    color: var(--poi-blue) !important;
                }
                
                /* Admin password change form */
                .password_change_form {
                    background: var(--poi-dark) !important;
                }
                
                /* Inline groups */
                .inline-group {
                    background: var(--poi-dark) !important;
                    border: 1px solid var(--poi-border) !important;
                }
                
                /* Object tools */
                .object-tools a {
                    background: transparent !important;
                    border: 1px solid var(--poi-blue) !important;
                    color: var(--poi-blue) !important;
                }
                
                .object-tools a:hover {
                    background: var(--poi-blue) !important;
                    color: var(--poi-black) !important;
                }
                
                /* Scrollbar styling for webkit */
                ::-webkit-scrollbar {
                    width: 8px;
                    height: 8px;
                }
                
                ::-webkit-scrollbar-track {
                    background: var(--poi-black) !important;
                }
                
                ::-webkit-scrollbar-thumb {
                    background: var(--poi-border) !important;
                    border-radius: 4px;
                }
                
                ::-webkit-scrollbar-thumb:hover {
                    background: var(--poi-blue) !important;
                }
            </style>
        '''
        context['extra_css'] = mark_safe(css)
        return context


# Replace Django's default admin site with our custom one
admin.site = MyAdminSite(name='admin')
