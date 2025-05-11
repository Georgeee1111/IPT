export interface Slide {
  title: string;
  description: string;
  image: string;
  thumb: string;
}

export interface SlideWithIndex extends Slide {
  originalIndex: number;
}
