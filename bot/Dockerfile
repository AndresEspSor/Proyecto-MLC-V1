# Use the official Node.js base image
FROM node:18.4.0-slim

# Install necessary dependencies, including Chrome
RUN apt-get update && apt-get install -y \
    g++ \
    make \
    wget \
    unzip \
    fonts-ipafont-gothic \
    fonts-wqy-zenhei \
    fonts-thai-tlwg \
    fonts-kacst \
    fonts-liberation \
    libappindicator1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libgcc1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    lsb-release \
    wget \
    xdg-utils \
    curl

# Set the working directory
WORKDIR /app

# Copy your Node.js application files to the container
COPY . /app

# Install Node.js dependencies using Yarn
RUN yarn install

# Install pm2 globally
RUN yarn global add pm2

# Expose the port your Express.js app will listen on
EXPOSE 3000

# Start your Express.js app with pm2 when the container runs
CMD ["pm2-runtime", "process.json"]