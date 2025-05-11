import { useState } from "react";
import { Link } from "react-router-dom";

interface NavbarProps {
  logo: string;
  links?: { label: string; href: string }[];
  showSearch?: boolean;
  onSearch?: (query: string) => void;
}

const Navbar: React.FC<NavbarProps> = ({
  logo,
  links = [],
  showSearch = false,
  onSearch,
}) => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");

  const toggleMobileMenu = () => setIsMobileMenuOpen((prev) => !prev);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (onSearch) onSearch(searchQuery);
  };

  return (
    <nav className="w-full bg-transparent text-white z-20 fixed top-0 left-0">
      <div className="max-w-screen-xl mx-auto flex items-center justify-between px-4 py-6">
        <div className="flex items-center">
          <img src={logo} alt="Logo" className="h-8" />
        </div>
        <div className="hidden md:flex space-x-6 items-center">
          {showSearch ? (
            <form onSubmit={handleSearchSubmit}>
              <input
                type="text"
                placeholder="Search..."
                className="px-3 py-1 rounded text-white"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </form>
          ) : (
            links.map((link) => (
              <Link
                key={link.label}
                to={link.href}
                className="hover:text-gray-400"
              >
                {link.label}
              </Link>
            ))
          )}
        </div>

        <button
          className="md:hidden p-2 text-white focus:outline-none"
          onClick={toggleMobileMenu}
        >
          <svg className="w-6 h-6" viewBox="0 0 24 24" stroke="currentColor">
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>
      </div>

      {isMobileMenuOpen && (
        <div className="md:hidden bg-black/80 px-4 py-4 space-y-4">
          {showSearch ? (
            <form onSubmit={handleSearchSubmit}>
              <input
                type="text"
                placeholder="Search..."
                className="w-full px-3 py-2 rounded text-black"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </form>
          ) : (
            links.map((link) => (
              <Link
                key={link.label}
                to={link.href}
                className="block text-white hover:text-gray-400"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                {link.label}
              </Link>
            ))
          )}
        </div>
      )}
    </nav>
  );
};

export default Navbar;
