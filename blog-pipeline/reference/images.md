# Images (stage 7) and alt text

Real job photos from `~/Downloads/client-photos/` are always first choice for the featured image (set in WordPress, 1200x675 minimum, 16:9). Never AI-generated people. Never present a generated image as an Example Electric job.

## Generated images (only when the user asks)

Higgsfield `generate_image` (load with `ToolSearch select:<Higgsfield prefix>generate_image`). Params: `model: nano_banana_pro`, `aspect_ratio: 16:9`, `resolution: 2k`, `count: 1`. Two modes:

| Mode | Prompt shape | Rules |
|---|---|---|
| `diagram` | "Clean technical diagram, white background, labelled: ..." with the exact figures from the checked ledger (e.g. "28 in rim height, 30 in horizontal, 5 ft disconnect distance") | Every label is a CONFIRMED value. No brand logos in the render (the brand card is separate). Caption says it is a diagram. |
| `realistic` | Photoreal scene of equipment or a setting, e.g. "outdoor spa GFCI disconnect mounted on a cedar post beside a patio, overcast Pacific Northwest light" | **No people.** No license numbers or company names in the image. Caption: "Illustration" or "Representative image", never "our install". Filename must not imply a job. |

Check the render before use: text legible, values match the ledger, nothing that reads as a real job.

## Alt text is part of the image, not an afterthought

**Every image the pipeline produces or places ships with three things, together:** the file (descriptive filename, no "master-electrician", no old phone number, no customer location), the **alt text**, and the caption. An image delivered without alt text is an unfinished stage 7.

Alt text rules (lint checks presence and length; the auditor checks quality):
- 8 to 16 words. Describes what is visible to someone who cannot see it. Not a keyword list.
- Names the type when generated: "Diagram of ..." / "Illustration of ...". Never implies a real customer job for generated images.
- No residential location tags. Metro level only for real job photos.
- No claims the image cannot support ("code-compliant install" is a claim; "spa disconnect on a post five feet from the tub" is a description).

Figure snippet (from template.md):
```html
<figure><img src="https://client.example/wp-content/uploads/YYYY/MM/<file>.jpg" alt="<8-16 words>" width="1200" height="675" loading="lazy"><figcaption>Diagram. <caption></figcaption></figure>
```
If the file is not uploaded yet, deliver the snippet with the alt text in the delivery table and omit the figure from the post; a placeholder `src` fails lint on purpose.

## GBP card (stage 9)

Default image for the GBP companion is the branded HTML card rendered from `OUTPUTS/branding-tool/` (1200x900 at `--force-device-scale-factor=3`, `sips -Z 2400`), using `Example_Electric-Gold_Logo_WA-NEW.png` only. Any code claim on the card is checked against `checked.md` like body copy. A real shoot photo is the alternative when the user wants a face.
