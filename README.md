[Digital-Forensics-README.md](https://github.com/user-attachments/files/29272577/Digital-Forensics-README.md)
# Digital Forensics Investigation

A digital forensics investigation of a disk image and network packet capture. Demonstrates the full forensic process: identification, acquisition, analysis, and reporting.

## Skills Demonstrated
Disk image analysis, email and web history examination, deleted file recovery, hash verification for chain of custody, network traffic analysis, and Python based log analysis.

## Tools
Autopsy 4.22.1, Wireshark, Python with Scapy, Windows Command Prompt

## Target
A forensic disk image labeled Forensics Case 2024.E01 and a network packet capture provided for cybersecurity training purposes. No live system was accessed.

---

## File System Analysis

![Autopsy file system](autopsy_filesystem.png)

---

## Deleted Files Recovery

![Autopsy deleted files](autopsy_deleted.png)

---

## Web History

![Autopsy web history](autopsy_webhistory.png)

---

## OS Accounts

![Autopsy OS accounts](autopsy_accounts.png)

---

## Email Analysis

![Autopsy emails](autopsy_emails.png)

---

## Hash Verification

![Hash MD5 and SHA1](hash_md5_and_sha1.png)

MD5 and SHA1 verified via certutil for chain of custody.

---

## Wireshark Network Traffic

![Wireshark HTTP filter](wireshark_http.png)

![Wireshark Conversations](wireshark_conversations.png)

---

## Python Log Analysis

![Python script](python_script.png)

![Python output](python_output.png)

Script flagged IPs with repeated connection attempts using Scapy.

---

## Summary

| Technique | Tool | Finding |
|---|---|---|
| Email Analysis | Autopsy | Suspicious communications recovered |
| Web History | Autopsy | Browsing activity including sensitive searches |
| OS Accounts | Autopsy | User accounts and login timestamps identified |
| Deleted Files | Autopsy | Files recovered from unallocated space |
| Hash Verification | certutil | MD5 and SHA1 documented for chain of custody |
| Network Traffic | Wireshark | HTTP and SYN traffic analyzed |
| Log Analysis | Python/Scapy | Suspicious IPs flagged by connection count |

## Ethics
This investigation used a disk image and packet capture provided for training purposes only. No live system or unauthorized data was accessed at any point.

## References
Casey, E. (2009). Handbook of digital forensics and investigation. Academic Press.  
Kent, K., Chevalier, S., Grance, T., & Dang, H. (2006). Guide to integrating forensic techniques into incident response (NIST Special Publication 800-86). https://doi.org/10.6028/NIST.SP.800-86  
Nelson, B., Phillips, A., & Steuart, C. (2009). Guide to computer forensics and investigations. Course Technology Press.  
Sanders, C., & Smith, J. (2014). Applied network security monitoring: collection, detection, and analysis. Syngress.
