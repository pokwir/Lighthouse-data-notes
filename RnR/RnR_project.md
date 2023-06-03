Title: Make better visualizations in python with ggplot.

Introduction:

Have you ever found yourself sitting through a data-heavy presentation that felt overwhelming and made your head hurt? I know the feeling all too well. But, don't worry! There is a solution to this problem. By incorporating compelling graphics into your data presentations, you can make a significant difference. Believe it or not, visuals have the power to enhance comprehension, engage the audience, simplify complex concepts, support data-driven storytelling, improve retention and recall, and enhance credibility and professionalism. So, if you want to transform your data presentations and make them more impactful and effective, it's time to start using visuals effectively.

As a data scientist, I understand that time can be a constraint when creating visuals for presentations. It can be a challenge to balance efficiency with visual appeal in the exploratory data analysis phase. However, there are strategies to create compelling visuals that effectively communicate your ideas to clients. Simple PyPlot charts may not be enough, but with the right approach, you can create visuals that are both efficient and visually appealing.

In this oh-so article, I'm going to show a demo of how you can create plots that will make your audience go "Aha!" instead of checking their Instagram feeds during your presentation. No more awkward PyPlot visuals that elicit yawns and glazed-over eyes. Let's dive into these magical secrets of creating plots that will leave a lasting impression on your audience.

First things first, lets install some packages. 
`pip install lets-plot`

And then ofcourse import the usual packages

```python 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
from lets_plot import *
LetsPlot.setup_html()
```

The data im using is available at this link: 

Lets start by creating a usual matplotlib plot for visualizing life expectancy and GDP percapita for the different countries. 

```python
plt.style.use('fivethirtyeight')

plt.figure(figsize=(12,8))
sns.scatterplot(x='gdp_cap', y='life_exp', hue='continent', data=df)
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Life Expectancy (years)')
plt.show()
```

The output would print this scatter plot. 

![](lets-plot-images/life_Exp_mat_plot.png)

Now, let's transform this plot that can enhance comprehension, keeping your audience engaged, and support your story. 

```python
p = ggplot(df, aes(x='gdp_cap', y='life_exp', color='continent', size = 'population')) + geom_point(alpha=0.9,show_legend= False, stat= 'identity') + \
        scale_color_viridis(option='D', direction=-1) + \
        scale_size(range = [1, 15]) + \
        ggtitle('GDP per capita and life expectancy') + \
            theme_classic() + \
                flavor_high_contrast_dark() + \
                scale_x_log10() + \
        xlab('GDP per capita') + ylab('Life expectancy') + \
        ggsize(1366, 768)
p
```

The first line, I instanciate the ggplot function and pass in my dataframe and the axes `aes`. I'm plotting gdp, life expectancy and the size of my geometry (more later) is the population and coloring by continent. I then add geometry type (geom_pint, this is a scatter plot in ggplot) and pass in alpha value, legend, and the most important argument stat = identity. The stat argument lets you create satistics from the data points, in this case I want the raw values (identity)

The second line is color theme, you can change the color to whatever you like or aligns with your presentation theme. 

The third line is the title. Fourth is canvas theme, I used classic (no grid lines and simple interface). The fith line is the flavour of the canvas, you can think of it as the theme too, I like high contrast dark for the black background that makes the colours pop and its easy to the eyes if you are presenting on zoom. The last two line are for the labels and size of the plot. 

And viola


![label](correlation.svg)

Okay. I'm sold, show me how:

-
