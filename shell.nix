{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      geojson
      httpx
      jinja2
      overpy
      pyproj
      pytest
      requests
      tqdm
    ]))
  ];
}
