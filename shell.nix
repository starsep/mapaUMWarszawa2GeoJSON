let
  # We pin to a specific nixpkgs commit for reproducibility.
  # Check for new commits at https://status.nixos.org.
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/b9014df496d5b68bf7c0145d0e9b0f529ce4f2a8.tar.gz") {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      geojson
      requests
      overpy
      pyproj
      requests
      tqdm
    ]))
  ];
}
