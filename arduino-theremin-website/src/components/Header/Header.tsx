import "./Header.css";

interface HeaderProps {
  title: string;
}
const Header = (props: HeaderProps) => {
  return (
    <header>
      <h1>{props.title}</h1>
      <h3 className="header-h3">How to build an Arduino theremin USB midi controller</h3>
    </header>
  );
};

export default Header;
