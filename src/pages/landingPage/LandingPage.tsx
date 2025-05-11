import { useEffect, useState } from "react";
import slidesData from "../../data/slides";
import Navbar from "../../components/general/Navbar";
import BackgroundImage from "../../components/landingPage/BackgroundImage";
import SlideText from "../../components/landingPage/SlideText";
import SlideThumbnails from "../../components/landingPage/SlideThumbnails";
import { navLinks } from "../../config/navigationConfig";
import { brandLogo } from "../../config/brandConfig";

const ITEMS_PER_PAGE = 3;

export default function LandingPage() {
  const [activeIndex, setActiveIndex] = useState(0);
  const activeSlide = slidesData[activeIndex];

  useEffect(() => {
    const imagePromises = slidesData.map((slide) => {
      const img = new Image();
      img.src = slide.image;
      return new Promise((resolve) => {
        img.onload = resolve;
      });
    });

    Promise.all(imagePromises);

    const interval = setInterval(() => {
      setActiveIndex((prevIndex) => (prevIndex + 1) % slidesData.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const reorderedSlides = [
    ...slidesData.slice(activeIndex),
    ...slidesData.slice(0, activeIndex),
  ];

  const currentSlides = reorderedSlides
    .slice(0, ITEMS_PER_PAGE)
    .map((slide, index) => ({ ...slide, originalIndex: index }));

  return (
    <div className="relative w-screen h-screen overflow-hidden">
      <Navbar logo={brandLogo} links={navLinks} />
      <BackgroundImage image={activeSlide.image} />
      <div className="absolute inset-0 bg-black/60 flex items-center justify-between px-16 text-white z-10 transition-opacity duration-1500 ease-in-out">
        <SlideText
          title={activeSlide.title}
          description={activeSlide.description}
        />
        <SlideThumbnails
          slides={currentSlides}
          activeIndex={activeIndex}
          onSelect={setActiveIndex}
        />
      </div>
    </div>
  );
}
