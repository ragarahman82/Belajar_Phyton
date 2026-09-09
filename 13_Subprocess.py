#Password Viewer
import subprocess
import re

output  = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    text=True,
    encoding="utf-8",
    errors="ignore"
)

Profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)

for profile in Profiles:
    profile = profile.strip()   
    details = subprocess.check_output(
        ["netsh", "wlan", "show", "profile", profile, "key=clear"],
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    password_match = re.search(
        r"Key Content\s*:\s*(.*)", details
    )
    password = password_match.group(1).strip() if password_match else "No Password"
    print(f"WI-FI: {profile}")
    print(f"Password: {password}")
    print("-" * 30)



