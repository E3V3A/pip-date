---
name: Bug Report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''


---
For new bugs and issues, please **make sure** to:
- [ ] check and search previous issues for similar or related problems.
- [ ] get info about your system configuration and environment, if relevant.
- [ ] include detailed information on what you did before the *error/issue* occurred.
- [ ] use code mark-down using 3 back-ticks (\`\`\`), to enclose multi-line code/input/output.
- [ ] include a **screenshot** for issues concerning *layouts, formatting* or other UI stuff. 
- [ ] If this is a request for an enhancement or other improvement, please state this clearly.


**Environment**
Please provide some information about your computer environment:

- [ ] OS:  
  `$W = (Get-CimInstance Win32_OperatingSystem); '{0} ({1})' -f $W.Caption, $W.Verson`  (On Windows)
  `uname -a` (On WSL or *nix based OS)
- [ ] Python version:
  `python -VV && python -c "import os; print('\n'.join([os.name, os.sys.platform]));"`
- [ ] pip version:  
  `pip -V`
- [ ] Terminal/Shell: (*powershell, pwsh, Windows Terminal, WSL* etc.)


<!-- Feel free to add more information about your environment here -->

**Description**
<!-- A clear and concise description of what the bug is. -->

**Expected behavior**
<!-- A clear and concise description of what you expected to happen. -->

**Actual Behaviour:**
<!-- A description of what actually happened. -->


**How to Reproduce**
<!-- Describe the steps to reproduce this bug. -->

1. Get package from '...'
2. Then run '...'
3. An error occurs.

**Output**

```
Paste the output of the steps above, including the commands themselves and
pip's output/traceback etc.
```

If the problem is graphical in nature, please add a screenshot.
<sub>(A picture is worth...)</sub>
