import type { Slide } from "../types/Slide";

import school1 from "../assets/images/landingPage/1st.jpg";
import school2 from "../assets/images/landingPage/2nd.jpg";
import school3 from "../assets/images/landingPage/3rd.jpg";
import school4 from "../assets/images/landingPage/4th.jpg";

const slides: Slide[] = [
  {
    title: "lorem ipsum",
    description: "Lorem ipsum dolor sit amet...",
    image: school1,
    thumb: school1,
  },
  {
    title: "lorem ipsum",
    description: "Lorem ipsum dolor sit amet...",
    image: school2,
    thumb: school2,
  },
  {
    title: "lorem ipsum",
    description: "Lorem ipsum dolor sit amet...",
    image: school3,
    thumb: school3,
  },
  {
    title: "lorem ipsum",
    description: "Lorem ipsum dolor sit amet...",
    image: school4,
    thumb: school4,
  },
];

export default slides;
