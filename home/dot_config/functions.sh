#!/bin/env bash

# Create a new directory and get into it
mkcd() {
  mkdir -p "$@"
  cd "$_";
}
