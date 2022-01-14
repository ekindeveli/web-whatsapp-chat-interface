from configobj import ConfigObj
import os
import sys


class OverrideConfigSpace(ConfigObj):
    def _write_line(self, indent_string, entry, this_entry, comment):
        """Write an individual line, for the write method"""
        # NOTE: the calls to self._quote here handles non-StringType values.
        if not self.unrepr:
            val = self._decode_element(self._quote(this_entry))
        else:
            val = repr(this_entry)
        return '%s%s%s%s%s' % (indent_string,
                               self._decode_element(self._quote(entry, multiline=False)),
                               self._a_to_u('='),
                               val,
                               self._decode_element(comment))


def profile_configobj():

    username = os.getlogin()
    pathname = os.path.dirname(sys.argv[0])

    a_filepath = rf'C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\profiles.ini'
    a_config = OverrideConfigSpace(a_filepath)

    try:
        for i in range(99):
            prof_checker = a_config[f'Profile{i}']
            name = prof_checker['Name']
            if name == "whatsweb":
                print("Firefox Profile Already Exists.")
                return
        prof_number_final = 0

    except KeyError as k:

        prof_number = str(k)
        prof_number_final = prof_number[-2]

    profile = {
        'Name': 'whatsweb',
        'IsRelative': '0',
        'Path': rf'{os.path.abspath(pathname)}\FirefoxProfile\rvzud5ty.whatsweb'
        }   # profile variable for if the profile path stays in WhatsEnteg folder

    a_config[f'Profile{prof_number_final}'] = profile
    a_config['General'] = {}
    a_config['General']['StartWithLastProfile'] = '0'
    a_config['General']['Version'] = '2'

    a_config.write()

    print("Firefox Profile Set Up Successfully.")
    return


profile_configobj()

