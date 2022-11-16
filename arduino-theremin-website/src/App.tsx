import "./App.css";

// Components
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import MainNavigation from "./components/MainNavigation/MainNavigation";
import VideoEmbed from "./components/VideoEmbed/VideoEmbed";
import Card from "./components/Card/Card";

function App() {
  return (
    <div className="App">
      <MainNavigation />
      <Header title="Arduino Theremin Website" />
      <main>
        <section>
          <h2>Circuit Diagram:</h2>
          <Card>
            <div className="container">
              <div className="column-1 box">
                <div className="card-container">
                  <h3 className="card-h3">
                    <strong>(Instructions coming soon!)</strong>
                  </h3>
                  <img
                    className="img-responsive circuit-img"
                    src="arduino_circuit_diagram.jpg"
                    alt="arduino circuit diagram"
                  />
                </div>
              </div>
              <div className="column-1 box">
                <div className="card-container">
                  <h3 className="card-h3">Required Components:</h3>
                  <ul className="component-list">
                    <li>Arduino Leonardo x1</li>
                    <li>HC-SR04 Ultrasonic Sensor x2</li>
                    <li>Full Sized Breadboard (830 tie-points) x1</li>
                    <li>Basic Yellow LED 5mm x1</li>
                    <li>220 Ohm Resistor x1</li>
                    <li>Mini Pushbutton Switch x1</li>
                    <li>10K Ohm Resistor x1</li>
                    <li>Breadboard Jumper Wires x14</li>
                  </ul>
                </div>
              </div>
            </div>
          </Card>
        </section>

        <section>
          <h2 id="video">Video demonstration:</h2>
          <VideoEmbed src="https://www.youtube.com/embed/SRdbWWPfvxk" />
        </section>

        <section>
          <h2 id="midi-messages">How MIDI messages work:</h2>
          <Card>
            <div className="midi-message-card-container">
              <h3 className="card-h3">Pitchbend MIDI messages</h3>

              <p>
                Pitchbend midi messages consist of 3 bytes: 1 status byte and 2
                data bytes.
              </p>
              <pre>11100000 + 01111111 + 01111111</pre>
              <pre>[status] [lsb data] [msb data]</pre>

              <p>
                Note that the status byte has 1 as the leftmost (most
                significant) bit and the data bytes have 0 as the leftmost bit.
                This allows you to send the status byte once and keep sending
                data bytes for the same parameter without resending the status
                byte. Data bytes therefore have only 7-bits because the leftmost
                bit is always 0. The high nibble (leftmost 4-bits) of the status
                byte is the type of midi message (0xE or 0111 is pitchbend in
                this case) and the low nibble (rightmost 4-bits) is the midi
                channel (0 to 15).
              </p>
              <p>
                The pitchbend value combines the 2 data bytes into a 14-bit
                unsigned integer with the following range:
              </p>

              <p>
                0x0000 is minimum pitch bend value (negative pitch bend) <br />
                0x2000 (8192 base 10) is middle pitch bend value (no pitch bend)
                <br />
                0x3FFF (16383 base 10) max pitch bend value (postive pitch bend){" "}
                <br />
              </p>
            </div>
          </Card>
          <Card>
            <div className="midi-message-card-container">
              <h3 className="card-h3">Volume MIDI messages</h3>

              <p>
                Volume MIDI messages are a type of continous controller (CC)
                MIDI message, which represents a range of values instead of a
                discrete on/off value like a note. They also consist of 3 bytes:
                1 status byte, 1 CC byte and 1 data byte.
              </p>
              <pre>10110000 + 00000111 + 01111111</pre>
              <pre>[status] [ CC ] [ data ]</pre>
              <p>
                The status byte value of 0xB0 or 10110000 indicates this is a
                continuous controller message for MIDI channel 0. The CC byte
                indicates the type of CC message (0x07 or 00000111 is channel
                volume). The data byte is the value of the message (from 0 to
                127).
              </p>
            </div>
          </Card>
        </section>
        <Card>
          <div className="midi-message-card-container">
            <h3 className="card-h3">Arduino MIDIUSB Library</h3>
            <p>
              The following library is used to allow the Arduino to send MIDI
              messages via USB, see links below:
            </p>
            <ul>
              <li>
                <a
                  className="card-a"
                  href="https://www.arduino.cc/reference/en/libraries/midiusb/"
                >
                  Arduino MIDIUSB library reference
                </a>
              </li>
              <li>
                <a
                  className="card-a"
                  href="https://github.com/arduino-libraries/MIDIUSB"
                >
                  MIDIUSB Github
                </a>
              </li>
            </ul>
          </div>
        </Card>
      </main>
      <Footer
        githubWebsiteLink="https://github.com/DrCBeatz/arduino-theremin"
        githubTitle="Arduino Theremin Github"
        authorWebsiteLink="https://drcbeatz.com"
        authorTitle="Dr. C. Beatz"
      />
    </div>
  );
}

export default App;
