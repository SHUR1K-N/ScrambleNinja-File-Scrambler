# ScrambleNinja: File Scrambler & Unscrambler

## Description & Usage
A tool that can scramble any file by rearranging the bytes it consists of—rendering it unreadable; and also unscramble any scrambled file (only if it was scrambled using this tool in the first place) by restoring the arrangement of bytes to be as the original, unscrambled file.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/ScrambleNinja-File-Scrambler/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, as a product of curiosity with byte re-arrangement and un-re-arrangement within files.

## File types tested so far & confirmed as fully supported
- **.EXE**
- **.FLAC**
- **.JPEG / .JPG**
- **.MKV**
- **.MOV**
- **.MP3**
- **.MP4**
- **.PDF**
- **.PNG**
- **.RAR**
- **.WAV**
- **.ZIP**

*You may test other file extensions/types and report them as supported/unsupported to update this list in the future.*

## File types not optimally supported / not recommended to scramble (yet)
### Microsoft Office files (.docx, .xlsx, etc.):
The tool successfully scrambles these files, but once they are *unscrambled*, Microsoft Excel/Word would see them as "corrupted or damaged". **However, Microsoft will also then ask if you would like to "fix" the contents of this unscrambled file, and upon choosing to do so, will be able to read the file as normal.**

This happens due to the byte-scrambling approach implemented in this tool. When the byte lines are scrambled, a pesky little "end-of-line / carriage-return" byte combination is left at the very end of the bytes list, which Microsoft Office applications apparently are quite strict about. When you choose to let Microsoft "fix" this, that final combination is simply removed by Microsoft. **Hence, technically, the scrambling and unscrambling work as ultimately intended; but the mechanism is just—for lack of a better word—a little "janky".**

### Plain text files:
Since this tool rearranges the *lines* of bytes in a file in order to scramble it, only the *line* arrangement of the plain text will be scrambled. This may impact the human readibility of the file by throwing a wrench in the typical sequential reading process, but the overall context may somewhat still be intelligible even if completely unordered.

For example, a .TXT file with the following lines:

<div align="center">

|Line #|Line Text                                            |
|:----:|-----------------------------------------------------|
|**1** |It was all a dream, I used to read Word Up! magazine |
|**2** |Salt-n-Pepa and Heavy D up in the limousine          |
|**3** |Hangin' pictures on my wall                          |
|**4** |Every Saturday Rap Attack, Mr. Magic, Marley Marl    |
|**5** |I let my tape rock 'til my tape popped               |
|**6** |Smokin' weed in Bambu, sippin' on Private Stock      |

</div>

... upon scrambling, becomes:

<div align="center">

|Line #|Line Text                                            |
|:----:|-----------------------------------------------------|
|**3** |Hangin' pictures on my wall                          |
|**2** |Salt-n-Pepa and Heavy D up in the limousine          |
|**1** |It was all a dream, I used to read Word Up! magazine |
|**6** |Smokin' weed in Bambu, sippin' on Private Stock      |
|**5** |I let my tape rock 'til my tape popped               |
|**4** |Every Saturday Rap Attack, Mr. Magic, Marley Marl    |

</div>

**Hence, it is not recommended to use this tool to scramble plain text files if your usage scenario is serious and/or your priority is confidentiality.**

## Note
ScrambleNinja is currently RAM-intensive (due to holding the bytes-to-scramble within a list). Hence, please ensure your system uses the 64-bit architecture *and* your Python installation is 64-bit as well for optimal performance. If either of these two criteria is not matched, ScrambleNinja may not work for file sizes upwards of ~2GBs since the 32-bit architecture and/or 32-bit installation Python will only allow 4GBs of RAM to be utilized no matter how many sticks you have installed (You will get **"MemoryError"** in the ScrambleNinja window if it fails).

You can read more about why 32-bit systems are limited to 4GBs of RAM utilization [here](https://superuser.com/questions/372881/is-there-a-technical-reason-why-32-bit-windows-is-limited-to-4gb-of-ram).

## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
