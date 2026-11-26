# Audio & Acoustics Project: Multiple Microphones Comb Filter Effect

An interactive simulation for the case of Multiple Microphones Comb Filter Effect.

When two microphones pick up the same sound source from different distances, each one receives the signal with a different delay, and mixing the two copies produces the comb filter effect. This Python desktop application lets you place two microphones and a source on a canvas, computes each microphone's distance and delay to the source, and plots the resulting delayed signals of a test recording. It was built by a two-person team in Digital Media Engineering and Technology (DMET).

## Features

- **Drag-and-drop scene**: move `Mic1`, `Mic2` and `Source` freely on a Tkinter canvas; positions update live and print to the terminal.
- **Distance and delay**: computes the distance from each microphone to the source and the delay as distance divided by a speed-of-sound constant of 331.29, shown in message boxes and drawn as lines on the canvas.
- **Measure without decay**: plots the left and right channels of the test WAV file, their spectrograms, and the left channel in dB shifted by each microphone's delay.
- **Measure with decay**: plots the channels and spectrograms, then applies a stepped, distance-based level change to each microphone's copy (from +6 below a distance of 10 to −20 at 80 and beyond) and overlays both delayed signals in one figure.
- **Delete lines and texts** to clear the canvas and start over without restarting the program.
- **Terminal log** of sample rate, number of samples, length in seconds and number of channels on every run.

## Tech stack

- Python 3
- Tkinter (GUI)
- NumPy (positions, distances, signal arrays)
- Matplotlib (waveforms, spectrograms, delayed-signal plots)
- `wave` from the standard library (WAV reading)
- `librosa`, `pydub` and `soundfile` are imported by `project.py`, so they must be installed for it to start

## Repository structure

```
.
├── project.py                            source code of the simulation
├── Alesis-Sanctuary-QCard-Crickets.wav   test sound source read by project.py
├── sound1.wav                            second test sound source
├── TECHNICAL REPORT.pdf                  technical report
├── TECHNICAL REPORT.docx                 technical report (Word source)
├── Video1.mp4                            short video of the simulation being tested
└── read_me.txt                           team and contents list
```

## How to run

1. Install Python 3 with Tkinter.
2. Install the libraries:

   ```
   pip install numpy matplotlib librosa pydub soundfile
   ```

3. From the repository root, run:

   ```
   python project.py
   ```

   The script opens `Alesis-Sanctuary-QCard-Crickets.wav` by a relative path, so it must be started from the folder that holds the file. It reads the audio as 16-bit stereo.

4. Drag the objects, then press **Measure Distance & Delay without Decay** or **Measure Distance & Delay with Decay**. Use **Delete Lines and Texts** to clear the canvas and **Destroy Window** to quit.

## Results

- [`Video1.mp4`](Video1.mp4) shows the simulation being tested: dragging the objects and the figures that open for each mode.
- [`TECHNICAL REPORT.pdf`](TECHNICAL%20REPORT.pdf) explains the simulation in detail. As it notes, the larger the distance, the more delay the signal has and the later it finishes.

## Team

- Abdelrahman Khaled Ahmed Hussin Abdelrahman: draggable objects, distance and delay calculations
- Youssef Ayman Abdelsabour: amplitude-to-dB conversion and the decay mode

## Author

Abdelrahman Abdelrahman — https://abdelrahman.eu
