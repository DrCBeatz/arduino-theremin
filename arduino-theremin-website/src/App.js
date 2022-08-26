import './App.css';

// Components
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import MainNavigation from "./components/MainNavigation/MainNavigation";
import VideoEmbed from './components/VideoEmbed/VideoEmbed';

function App() {
  return (
    <div className="App">

      <MainNavigation />
      <Header title="Arduino Theremin Website" />

      <main>
          <VideoEmbed src="https://www.youtube.com/embed/uJBxB8OOZTo" />
      </main>

      {/* <footer className="text-center">
          <a href="https://github.com/DrCBeatz/arduino-theremin" target="_blank" rel="noreferrer">Arduino Theremin Github</a>
          <p>Website by <a href="https://drcbeatz.com" target="_blank" rel="noreferrer">Dr. C. Beatz</a></p>
      </footer> */}

      <Footer githubWebsiteLink="https://github.com/DrCBeatz/arduino-theremin" githubTitle="Arduino Theremin Github" authorWebsiteLink="https://drcbeatz.com" authorTitle="Dr. C. Beatz"/>
    </div>
  );
}

export default App;
