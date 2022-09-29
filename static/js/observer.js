/**
 * Zoom images
*/
let subTopicContainer = document.getElementById('subtopic-container');
if (subTopicContainer) {
    subTopicContainer.addEventListener('click', function(e) {
        const tgt = e.target;
        tgt.tagName == 'IMG' ? tgt.classList.toggle('zoomed') : void 0;
    });
};
const setupClickAndScrollClassToggle = () => {            
    document.addEventListener('scroll', (event)=> {
        let elements = Array.from(document.querySelectorAll('img'));
        toggleCSSclasses(elements, 'zoomed');
    });
}
/**
 * toggleCSSclasses
 * @params 
 * elems : elements
 * ...cls : classes to check for/toggle
 */
const toggleCSSclasses = (elems, ...cls) => elems.forEach(el => el.classList.contains(cls) ? el.classList.toggle(cls) : void 0);

const scrollToTargetAdjusted = () => {
    /**
     * Offsets subtopic elements on auto scroll when subtopic links are clicked
     */
    let elements = Array.from(document.querySelectorAll('.subtopic-link'));
    if (elements) {
        elements.forEach(element => element.addEventListener('click', ()=> {

            toggleCSSclasses(elements, 'active', 'connected');
            let subTopic = element.dataset.topic;
            let topicElem = document.getElementById(subTopic);
            let headerOffset = 90;
            let elementPosition = topicElem.getBoundingClientRect().top;
            let offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            const scrolled = new Promise((resolve, reject) => {
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
                setTimeout(() => {
                    resolve(element);
                }, 250);
            });
            const connected = new Promise((resolve, reject) => {
                setTimeout(() => {
                    resolve(element);
                }, 525);
            });
            scrolled.then((element) => {
                element.classList.add('active');
            });
            connected.then((element) => {
                element.classList.add('connected');
            });
        }));
    }
};
scrollToTargetAdjusted();

function setup() {
    /**
     * Trigger active/connected classes for subtopic links on page scroll
     */
    const options = {
        threshold: 1,
        rootMargin: "-10px 0px 0px 0px",
    };
    const elements = Array.from(document.querySelectorAll('.subtopic-link'));
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            const id = entry.target.dataset.card;
            const link = document.querySelector(`[data-topic="${id}"]`);
            const intersecting = entry.isIntersecting;
            if (intersecting) {
                toggleCSSclasses(elements, 'active', 'connected');
                link.classList.add('active', 'connected');
            }
            else link.classList.remove('active', 'connected');
        })
    }, options);
    const cards = document.querySelectorAll('.topic-card');
    if(cards) cards.forEach(card => observer.observe(card));
};

window.addEventListener('DOMContentLoaded', () => {
    setup();
    setupClickAndScrollClassToggle();
}); 