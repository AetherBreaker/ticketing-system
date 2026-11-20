import { _t } from "@web/core/l10n/translation";
import { browser } from "@web/core/browser/browser";
import { cookie } from "@web/core/browser/cookie";
import { registry } from "@web/core/registry";

// The page picks its stylesheet on the server from this cookie (IrHttp.color_scheme), so a switch needs a reload.
function darkModeItem() {
    const isDark = cookie.get("color_scheme") === "dark";
    return {
        type: "switch",
        id: "color_scheme.switch_theme",
        description: _t("Dark mode"),
        isChecked: isDark,
        callback: () => {
            cookie.set("color_scheme", isDark ? "light" : "dark");
            browser.location.reload();
        },
        sequence: 30,
    };
}

registry.category("user_menuitems").add("dark_mode", darkModeItem);
