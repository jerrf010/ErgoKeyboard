from kmk.bootcfg import bootcfg

bootcfg(
    # optional:
    sense: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
    source: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
    autoreload: bool = True,
    boot_device����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������alse,
    storage: bool = True,
    usb_id: Optional[dict] = {},
    **kwargs,
) -> bool