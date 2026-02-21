#!/usr/bin/env python

content = '''{% extends 'base.html' %}
{% load static %}

{% block title %}About - HARSHIT RAJ{% endblock %}

{% block content %}
<div class="bg-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="mb-12">
            <p class="text-xl text-gray-600 text-center max-w-3xl mx-auto">
                I am a passionate Full Stack Developer and Cybersecurity Enthusiast currently pursuing my B.Tech in Computer Science and Engineering at Lovely Professional University. 
                With hands-on experience in Python, Django, React, and various cybersecurity tools, I am eager to contribute to innovative projects and continue learning new technologies.
            </p>
        </div>

        <div class="mt-16">
            <h2 class="text-3xl font-bold text-center mb-8">Skills</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <div class="bg-blue-50 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-4">Languages</h3>
                    <ul class="list-disc list-inside space-y-2 text-gray-600">
                        <li>Python</li>
                        <li>Java</li>
                        <li>C++</li>
                    </ul>
                </div>

                <div class="bg-blue-50 p-6 rounded-lg shadow-md"> 
                    <h3 class="text-xl font-semibold mb-4">Frameworks</h3>
                    <ul class="list-disc list-inside space-y-2 text-gray-600">
                        <li>React</li>
                        <li>Django</li>
                    </ul>
                </div>

                <div class="bg-blue-50 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-4">Tools & Platforms</h3>
                    <ul class="list-disc list-inside space-y-2 text-gray-600">
                        <li>MySQL</li>
                        <li>Git</li>
                        <li>AWS</li>
                        <li>Kali Linux</li>
                    </ul>
                </div>

                <div class="bg-blue-50 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-4">Soft Skills</h3>
                    <ul class="list-disc list-inside space-y-2 text-gray-600">
                        <li>Creative</li>
                        <li>Problem solver</li>
                        <li>Active Listener</li>
                        <li>Adaptability</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="mt-16">
            <h2 class="text-3xl font-bold text-center mb-8">Internships</h2>
            <div class="space-y-8">
                
                <div class="bg-white border-l-4 border-indigo-500 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-1">Conquest Tech Solutions</h3>
                    <p class="text-sm text-gray-500 mb-4">Intern Computer Analyst | June-July 2023</p>
                    <ul class="list-disc list-inside space-y-2 text-gray-600 mb-4">
                        <li>Conducted software test evaluations, identified issues, and reviewed system functionalities</li>
                        <li>Created and maintained structured documentation, reports, and workflow summaries</li>
                        <li>Interacted with team members to understand requirements</li>
                    </ul>
                    <p class="text-sm text-gray-500"><strong>Tech Used:</strong> Git/Github, MS Office, Bug Tracking Systems, Google workspace, Google Meet</p>
                </div>

                <div class="bg-white border-l-4 border-indigo-500 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-1">Coincent.ai</h3>
                    <p class="text-sm text-gray-500 mb-4">Cyber Security & Ethical Hacking Training | January-March 2023</p>
                    <ul class="list-disc list-inside space-y-2 text-gray-600 mb-4">
                        <li>Gained Hands-on experience in network security, penetration testing, and threat analysis</li>
                        <li>Worked with tools to identify vulnerabilities and understand secure solutions</li>
                        <li>Improved understanding of system security and ethical hacking principles</li>
                    </ul>
                    <p class="text-sm text-gray-500"><strong>Tech Used:</strong> Kali Linux Tools, Nmap, Burp Suite, Wireshark, Hydra, SQL map</p>
                </div>
            </div>
        </div>

        <div class="mt-16">
            <h2 class="text-3xl font-bold text-center mb-8">Projects</h2>
            <div class="space-y-8">
                
                <div class="bg-white border-l-4 border-indigo-500 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-1">ArtiQuery (HBS Chats) - AI Chatbot</h3>
                    <p class="text-sm text-gray-500 mb-4">February-April 2024</p>
                    <p class="text-gray-600 mb-4">ArtiQuery is an AI chatbot that works both online and offline. It can answer questions, create images, and handle voice input and output. Uses ML and AI APIs along with Python libraries.</p>
                    <p class="text-sm text-gray-500"><strong>Tech Used:</strong> Python, Kivy, API Integration, Speech Recognition, TTS, Image Generation, GUI Development</p>
                </div>

                <div class="bg-white border-l-4 border-indigo-500 p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-1">Cyber Security Labs</h3>
                    <p class="text-sm text-gray-500 mb-4">January-March 2023</p>
                    <p class="text-gray-600 mb-4">Practical cyber security exercises focusing on identifying system and network vulnerabilities, penetration testing, and threat analysis.</p>
                    <p class="text-sm text-gray-500"><strong>Tech Used:</strong> Kali Linux, Nmap, Burp Suite, Penetration Testing</p>
                </div>
            </div>
        </div>

        <div class="mt-16">
            <h2 class="text-3xl font-bold text-center mb-8">Certificates</h2>
            <ul class="space-y-4 text-gray-700">
                <li>Master Generative AI & Generative AI tools by Infosys Springboard (Aug 2025)</li>
                <li>Privacy and Security in Online Social Media by NPTEL (April 2025)</li>
                <li>Amazon Web Service (AWS) Certified by Infosys Springboard (April 2024)</li>
                <li>Fundamentals of Network Communication by University of Colorado, Coursera (Sept 2024)</li>
                <li>GCP Cloud Digital Leader Certification by KodeKloud (April 2023)</li>
                <li>Cyber Security and Ethical Hacking by Coincent.ai (March 2023)</li>
            </ul>
        </div>

        <div class="mt-16 mb-12">
            <h2 class="text-3xl font-bold text-center mb-8">Education</h2>
            
            <div class="bg-blue-50 border-l-4 border-indigo-500 p-6 rounded-lg shadow-md mb-4">
                <h3 class="text-xl font-bold mb-1">Lovely Professional University</h3>
                <p class="text-sm text-gray-500 mb-2">Phagwara, Punjab | Since August 2024</p>
                <p class="text-gray-600">Bachelor of Technology - Computer Science and Engineering; CGPA: 6.65</p>
            </div>

            <div class="bg-blue-50 border-l-4 border-indigo-500 p-6 rounded-lg shadow-md">
                <h3 class="text-xl font-bold mb-1">Lovely Professional University</h3>
                <p class="text-sm text-gray-500 mb-2">Phagwara, Punjab | August 2021 - June 2024</p>
                <p class="text-gray-600">Diploma Computer Science and Engineering; CGPA: 7.3</p>
            </div>
        </div>

    </div>
</div>
{% endblock %}
'''

with open('templates/projects_app/about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('about.html created successfully!')
