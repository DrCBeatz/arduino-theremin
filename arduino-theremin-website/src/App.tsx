import './App.css';

// Components
import { Header } from "./components/Header/Header";
import { Footer } from "./components/Footer/Footer";
import { MainNavigation } from "./components/MainNavigation/MainNavigation";
import { VideoEmbed } from './components/VideoEmbed/VideoEmbed';

function App() {
  return (
    <div className="App">

      <MainNavigation />
      <Header title="Arduino Theremin Website" />

      <main className="text-center">
          <img className="leonardo-arduino-img" src="arduino-leonardo.png" alt="Arduino Uno"/>
          <img height="200px" src="HC-SR04.jpg" alt="HC-SR04 ultrasonic sensor" />
          <VideoEmbed src="https://www.youtube.com/embed/uJBxB8OOZTo" />
      </main>

      <Footer githubWebsiteLink="https://github.com/DrCBeatz/arduino-theremin" githubTitle="Arduino Theremin Github" authorWebsiteLink="https://drcbeatz.com" authorTitle="Dr. C. Beatz"/>
    </div>
  );
}

export default App;
