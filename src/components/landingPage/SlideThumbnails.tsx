import type { SlideWithIndex } from "../../types/Slide";

interface SlideThumbnailsProps {
  slides: SlideWithIndex[];
  activeIndex: number;
  onSelect: (index: number) => void;
}

export default function SlideThumbnails({
  slides,
  activeIndex,
  onSelect,
}: SlideThumbnailsProps) {
  return (
    <div className="absolute bottom-0 right-0 flex gap-4 overflow-x-auto p-4">
      {slides.map((slide, i) => (
        <button
          key={i}
          onClick={() => onSelect(slide.originalIndex)}
          className={`w-24 h-24 bg-cover bg-center rounded-xl border-2 transition-all duration-300 ease-in-out cursor-pointer${
            slide.originalIndex === activeIndex
              ? "border-white opacity-70 hover:opacity-100"
              : "border-transparent opacity-100 scale-105"
          }`}
          style={{ backgroundImage: `url(${slide.thumb})` }}
        ></button>
      ))}
    </div>
  );
}
