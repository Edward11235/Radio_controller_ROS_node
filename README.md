# Graupner Signal Publisher

### Udev Rule for Arduino Nano

To ensure consistent naming of your Arduino Nano device, you can create a udev rule. This will allow the device to always appear at `/dev/arduino`.

1. **Identify Your Arduino Nano**

    ```sh
    lsusb
    ```

2. **Create the Udev Rule**

    ```sh
    sudo nano /etc/udev/rules.d/99-arduino-nano.rules
    # or
    sudo nano /etc/udev/rules.d/99-arduino-mega.rules
    ```

3. **Add the Following Rule**

    ```sh
    SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="arduino"
    or
    SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0042", SYMLINK+="arduino"
    ```

4. **Reload the Udev Rules**

    ```sh
    sudo udevadm control --reload-rules
    sudo udevadm trigger
    ```
# Radio_controller_ROS_node
