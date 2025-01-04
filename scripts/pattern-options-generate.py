#!/usr/bin/env python3


def main():
    # Read in all the patterns
    options = []
    set_actions = []
    with open("pattern-options.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                pattern, name = line.split(":")
                name = name.strip()
                options.append(f'      - "{name}"')
                set_actions.append(
                    f'          if (x.compare(std::string{{"{name}"}}) == 0) {{ id(dmx_2).set_level({float(pattern)/255}); }}'
                )

    options.sort()

    print(f"""\
    # Generated using pattern-options-generate.py
    options:
{'\n'.join(options)}
    set_action:
      - lambda: |-
{'\n'.join(set_actions)}
          """)


if __name__ == "__main__":
    main()
