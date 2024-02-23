---
theme: dashboard
title: Earthquakes
toc: false
---

```js
const quakes = FileAttachment("data/quakes.csv").csv()
```

## Earthquakes

Here are some earthquakes.

Here is a plot of all the earthquakes.

```js
Plot.plot({
  projection: {
    type: "orthographic",
    rotate: [110, -30],
  },
  marks: [
    Plot.graticule(),
    Plot.sphere(),
    // Plot.geo(land, { stroke: "var(--theme-foreground-faint)" }),
    Plot.dot(quakes, {
      x: "longitude",
      y: "latitude",
      r: "magnitude",
      stroke: "#f43f5e",
    }),
  ],
})
```
