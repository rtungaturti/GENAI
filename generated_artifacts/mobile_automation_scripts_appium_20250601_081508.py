# Mobile Automation Scripts for Google Home Page

## Page Object Model

```java
// GoogleHomePage.java

import io.appium.java_client.MobileElement;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.iOSFindBy;
import io.appium.java_client.pagefactory.PageFactory;

public class GoogleHomePage {
    @AndroidFindBy(xpath = "//textarea[@name='q']")
    @iOSFindBy(xpath = "//textarea[@name='q']")
    private MobileElement searchBox;

    @AndroidFindBy(xpath = "//input[@name='btnK']")
    @iOSFindBy(xpath = "//input[@name='btnK']")
    private MobileElement googleSearchButton;

    @AndroidFindBy(xpath = "//a[@href='https://about.google/?fg=1&utm_source=google-IN&utm_medium=referral&utm_campaign=hp-header']")
    @iOSFindBy(xpath = "//a[@href='https://about.google/?fg=1&utm_source=google-IN&utm_medium=referral&utm_campaign=hp-header']")
    private MobileElement aboutLink;

    // Other elements...

    public GoogleHomePage(AppiumDriver<MobileElement> driver) {
        PageFactory.initElements(driver, this);
    }

    public void enterSearchQuery(String query) {
        searchBox.sendKeys(query);
    }

    public void clickGoogleSearch() {
        googleSearchButton.click();
    }

    public void clickAboutLink() {
        aboutLink.click();
    }
}
```

## Android Configuration and Test Script

```java
// AndroidGoogleHomePageTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URL;

public class AndroidGoogleHomePageTest {
    private AppiumDriver<MobileElement> driver;
    private GoogleHomePage googleHomePage;

    @BeforeTest
    public void setup() throws MalformedURLException {
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("deviceName", "Android Emulator");
        capabilities.setCapability("automationName", "UiAutomator2");
        capabilities.setCapability("browserName", "Chrome");

        driver = new RemoteWebDriver(new URL("http://localhost:4723/wd/hub"), capabilities);
        googleHomePage = new GoogleHomePage(driver);
    }

    @Test
    public void testGoogleHomePage() {
        googleHomePage.enterSearchQuery("Appium");
        googleHomePage.clickGoogleSearch();
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
    }
}
```

## iOS Configuration and Test Script

```java
// iOSGoogleHomePageTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URL;

public class iOSGoogleHomePageTest {
    private AppiumDriver<MobileElement> driver;
    private GoogleHomePage googleHomePage;

    @BeforeTest
    public void setup() throws MalformedURLException {
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("platformName", "iOS");
        capabilities.setCapability("deviceName", "iPhone Simulator");
        capabilities.setCapability("automationName", "XCUITest");
        capabilities.setCapability("browserName", "Safari");

        driver = new RemoteWebDriver(new URL("http://localhost:4723/wd/hub"), capabilities);
        googleHomePage = new GoogleHomePage(driver);
    }

    @Test
    public void testGoogleHomePage() {
        googleHomePage.enterSearchQuery("Appium");
        googleHomePage.clickGoogleSearch();
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
    }
}
```

## Test Cases

### Touch Gestures

```java
// TouchGesturesTest.java

import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.touch.offset.PointOption;

public class TouchGesturesTest extends GoogleHomePage {
    @Test
    public void testTapGesture() {
        new TouchAction(driver).tap(PointOption.point(100, 100)).perform();
    }

    @Test
    public void testSwipeGesture() {
        new TouchAction(driver).swipe(PointOption.point(100, 100), PointOption.point(200, 200)).perform();
    }

    @Test
    public void testPinchGesture() {
        new TouchAction(driver).pinchOpen(PointOption.point(100, 100), PointOption.point(200, 200)).perform();
    }
}
```

### Device Orientation Changes

```java
// DeviceOrientationTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class DeviceOrientationTest extends GoogleHomePage {
    @Test
    public void testPortraitOrientation() {
        ((AppiumDriver<MobileElement>) driver).rotate(ScreenOrientation.PORTRAIT);
    }

    @Test
    public void testLandscapeOrientation() {
        ((AppiumDriver<MobileElement>) driver).rotate(ScreenOrientation.LANDSCAPE);
    }
}
```

### App Lifecycle Testing

```java
// AppLifecycleTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class AppLifecycleTest extends GoogleHomePage {
    @Test
    public void testBackgroundForeground() {
        driver.backgroundApp(5);
        driver.activateApp();
    }
}
```

### Network Condition Testing

```java
// NetworkConditionTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class NetworkConditionTest extends GoogleHomePage {
    @Test
    public void testOfflineOnline() {
        ((AppiumDriver<MobileElement>) driver).setNetworkConnection(new NetworkConnection(0));
        ((AppiumDriver<MobileElement>) driver).setNetworkConnection(new NetworkConnection(6));
    }
}
```

### Device-Specific Testing

```java
// DeviceSpecificTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class DeviceSpecificTest extends GoogleHomePage {
    @Test
    public void testDifferentScreenSizes() {
        // Perform actions on different screen sizes
    }
}
```

### Mobile Browser Testing

```java
// MobileBrowserTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class MobileBrowserTest extends GoogleHomePage {
    @Test
    public void testMobileBrowser() {
        // Perform actions on mobile browser
    }
}
```

### Accessibility Testing

```java
// AccessibilityTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class AccessibilityTest extends GoogleHomePage {
    @Test
    public void testAccessibility() {
        // Perform accessibility checks
    }
}
```

## Performance Testing

```java
// PerformanceTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class PerformanceTest extends GoogleHomePage {
    @Test
    public void testPerformance() {
        // Perform performance checks
    }
}
```

## Cross-Platform Strategies

```java
// CrossPlatformTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class CrossPlatformTest extends GoogleHomePage {
    @Test
    public void testCrossPlatform() {
        // Perform actions on both Android and iOS platforms
    }
}
```

## Mobile-Specific Assertions and Validations

```java
// MobileAssertionsTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class MobileAssertionsTest extends GoogleHomePage {
    @Test
    public void testMobileAssertions() {
        // Perform mobile-specific assertions
    }
}
```

## Mobile Performance Testing

```java
// MobilePerformanceTest.java

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class MobilePerformanceTest extends GoogleHomePage {
    @Test
    public void testMobilePerformance() {
        // Perform mobile performance checks
    }
}
```